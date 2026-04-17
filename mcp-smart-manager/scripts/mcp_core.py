import json
import os
import sys

CONFIG_PATH = "/Users/georgesouza/.gemini/antigravity/mcp_config.json"
REGISTRY_PATH = "/Users/georgesouza/.gemini/antigravity/mcp_registry.json"

# Tool counts (Manual audit based on last analysis)
TOOL_COUNTS = {
    "github-mcp-server": 41,
    "GitKraken": 23,
    "notebooklm": 38,
    "genkit-mcp-server": 10,
    "cloudrun": 8,
    "_prisma-mcp-server": 4,
    "google-developer-knowledge": 2,
    "sequential-thinking": 1,
    "built-ins": 15 # Internal to Antigravity, but we count them for safety
}

# Base servers that should NEVER be disabled
BASE_SERVERS = ["github-mcp-server", "sequential-thinking"]

PROFILES = {
    "research": ["notebooklm", "google-developer-knowledge"],
    "ops": ["GitKraken", "cloudrun", "_prisma-mcp-server"],
    "ai-dev": ["genkit-mcp-server"],
    "minimal": []
}

def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def get_active_tool_count(config):
    count = TOOL_COUNTS["built-ins"]
    servers = config.get("mcpServers", {})
    for name, cfg in servers.items():
        if not cfg.get("disabled", False):
            count += TOOL_COUNTS.get(name, 0)
    return count

def list_servers():
    registry = load_json(REGISTRY_PATH)
    config = load_json(CONFIG_PATH)
    servers = registry.get("mcpServers", {})
    
    print(f"{'SERVER':<30} | {'TOOLS':<5} | {'STATUS':<10} | {'BASE'}")
    print("-" * 65)
    
    active_servers = config.get("mcpServers", {})
    
    for name in servers:
        tools = TOOL_COUNTS.get(name, 0)
        is_active = not active_servers.get(name, {}).get("disabled", False)
        status = "ACTIVE" if is_active else "DISABLED"
        is_base = "*" if name in BASE_SERVERS else ""
        print(f"{name:<30} | {tools:<5} | {status:<10} | {is_base}")
    
    print("-" * 65)
    print(f"Total Active Tools: {get_active_tool_count(config)}/100")

def apply_profile(profile_name):
    if profile_name not in PROFILES:
        print(f"Error: Profile '{profile_name}' not found.")
        return

    registry = load_json(REGISTRY_PATH)
    config = load_json(REGISTRY_PATH) # Start fresh from registry
    
    servers = config.get("mcpServers", {})
    to_enable = PROFILES[profile_name] + BASE_SERVERS
    
    for name in servers:
        if name in to_enable:
            servers[name]["disabled"] = False
        else:
            servers[name]["disabled"] = True
            
    total = get_active_tool_count(config)
    if total > 100:
        print(f"Error: Profile '{profile_name}' would result in {total} tools (limit 100).")
        return

    save_json(CONFIG_PATH, config)
    print(f"Profile '{profile_name}' applied successfully. ({total}/100 tools)")

def toggle_server(name, enable=True):
    config = load_json(CONFIG_PATH)
    servers = config.get("mcpServers", {})
    
    if name not in servers:
        # Try to pull from registry
        registry = load_json(REGISTRY_PATH)
        if name in registry.get("mcpServers", {}):
            servers[name] = registry["mcpServers"][name]
        else:
            print(f"Error: Server '{name}' not found.")
            return

    servers[name]["disabled"] = not enable
    
    total = get_active_tool_count(config)
    if total > 100 and enable:
        print(f"Warning: Total tools now {total}/100. Disabling other servers might be needed.")
    
    save_json(CONFIG_PATH, config)
    print(f"Server '{name}' is now {'ENABLED' if enable else 'DISABLED'}. Total: {total}/100")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 mcp_core.py [list|profile <name>|enable <name>|disable <name>]")
        sys.exit(1)
        
    cmd = sys.argv[1]
    if cmd == "list":
        list_servers()
    elif cmd == "profile" and len(sys.argv) > 2:
        apply_profile(sys.argv[2])
    elif cmd == "enable" and len(sys.argv) > 2:
        toggle_server(sys.argv[2], True)
    elif cmd == "disable" and len(sys.argv) > 2:
        toggle_server(sys.argv[2], False)
    else:
        print("Unknown command or missing arguments.")
