import os
from fabric.api import *
from fabric.colors import *
from fabric.utils import *
from fabric.decorators import *
from fabric.context_manager import *

def build(opts):
  if opts == 'deps':
    local("")
elif opts == '':
    local("")
  else:
		local("echo 'Invalid Build Option'")
