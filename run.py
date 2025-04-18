"""
Script to run all components of the Travel Explorer application
"""
import os
import sys
import argparse
import subprocess
import time
import signal
import logging
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Global variables
processes = []

def signal_handler(sig, frame):
    """Handle Ctrl+C by stopping all processes."""
    logger.info("Shutting down...")
    for process in processes:
        try:
            process.terminate()
            logger.info(f"Terminated process: {process.args}")
        except:
            pass
    sys.exit(0)

def run_mcp_server(port):
    """Run the MCP server."""
    cmd = [sys.executable, "mcp_server.py"]
    env = os.environ.copy()
    env["PORT"] = str(port)
    
    logger.info(f"Starting MCP server on port {port}...")
    process = subprocess.Popen(cmd, env=env)
    processes.append(process)
    return process

def run_api_server(port):
    """Run the FastAPI server."""
    cmd = [sys.executable, "-m", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", str(port), "--reload"]
    
    logger.info(f"Starting API server on port {port}...")
    process = subprocess.Popen(cmd)
    processes.append(process)
    return process

def run_streamlit(port, api_url=None, mcp_url=None):
    """Run the Streamlit app."""
    cmd = [sys.executable, "-m", "streamlit", "run", "app.py", "--server.port", str(port)]
    env = os.environ.copy()
    
    if api_url:
        env["API_URL"] = api_url
    if mcp_url:
        env["MCP_SERVER_URL"] = mcp_url
    
    logger.info(f"Starting Streamlit app on port {port}...")
    process = subprocess.Popen(cmd, env=env)
    processes.append(process)
    return process

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Run the Travel Explorer application")
    parser.add_argument("--mcp-port", type=int, default=8080, help="Port for the MCP server")
    parser.add_argument("--api-port", type=int, default=8000, help="Port for the API server")
    parser.add_argument("--streamlit-port", type=int, default=8501, help="Port for the Streamlit app")
    parser.add_argument("--no-mcp", action="store_true", help="Don't run the MCP server")
    parser.add_argument("--no-api", action="store_true", help="Don't run the API server")
    parser.add_argument("--no-streamlit", action="store_true", help="Don't run the Streamlit app")
    
    args = parser.parse_args()
    
    # Set up signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    # Start the servers
    api_url = f"http://localhost:{args.api_port}/api"
    mcp_url = f"http://localhost:{args.mcp_port}"
    
    if not args.no_mcp:
        mcp_process = run_mcp_server(args.mcp_port)
        logger.info("Waiting for MCP server to start...")
        time.sleep(2)
    
    if not args.no_api:
        api_process = run_api_server(args.api_port)
        logger.info("Waiting for API server to start...")
        time.sleep(2)
    
    if not args.no_streamlit:
        streamlit_process = run_streamlit(args.streamlit_port, api_url, mcp_url)
    
    logger.info("All services started. Press Ctrl+C to exit.")
    
    # Wait for all processes to complete
    for process in processes:
        process.wait()

if __name__ == "__main__":
    main()