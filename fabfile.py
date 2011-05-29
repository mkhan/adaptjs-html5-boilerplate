import os
from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from fabric.decorators import *


def build(opts):
  if opts == "":
    pass
  elif opts == "":
    pass
  else:
    local("echo "Invalid Build Option"")
    
