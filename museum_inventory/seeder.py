from inventory.models import Tool, Borrower
import random

def seed_tools():
    tools = [('computer', 'macbook'), ('science', 'chemistry set'),
             ('cleaning','polishing rag'), ('fancyness','monocle'),
             ('science','magnifying glass'), ('engineering','robot'),
             ('engineering','3d printer'), ('magic', 'exhibit that comes to life')]
    for idx in range(100):
        random.shuffle(tools)
        tool_type = tools[0][1]
        tool_group = 'random'
        new_tool = Tool.create.create_tool(tool_type, tool_group)
        new_tool.save()
