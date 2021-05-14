import sys
sys.path.append("./modules/")

import hello
import deeper


hello_output = f"hello module returns: ${hello.world()}"
world_output = f"deeper module returns: ${deeper.recursive_success()}"