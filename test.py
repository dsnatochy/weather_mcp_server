import subprocess

def test_mcp_stdio():
    proc = subprocess.Popen(
        ["uv", "run" "/Users/dnatochy/development/work/mcp/weather/weather.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Construct a valid MCP/LSP request (e.g., initialize request)
    request = (
        "Content-Length: 75\r\n"
        "\r\n"
        '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}'
    )

    proc.stdin.write(request)
    proc.stdin.flush()

    response = proc.stdout.readline()
    print("Server responded:", response)

    proc.terminate()

test_mcp_stdio()
