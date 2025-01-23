# pyGL840

## Feature

- Write data in csv file
- Push data to mongoDB in the format of HSQuickLook.

## Installation

The Installation is very simple. Just download distribution file, and execute the following command.

  `pip install pyGL840-2.0.tar.gz`
  
If you want to use HSQuickLook, sound notification and slack notification, you need to add the following commands.

  `pip install pyGL840-2.0.tar.gz[mongo]` (HSQuickLook)

  `pip install pyGL840-2.0.tar.gz[sound]` (Sound notification)
  
  `pip install pyGL840-2.0.tar.gz[slack]` (Slack notification)
  
  `pip install pyGL840-2.0.tar.gz[mongo,sound,slack]` (All)

### Requirements

All the requirements can be installed automatically when you install pyGL840 using pip.

- requests

  Python module for transmitting via HTTP (Mandatory)

#### For HSQuickLook

If you use HSQuickLook(<https://github.com/odakahirokazu/HSQuicklook>), you must also install below.

- HSQuickLook
  Multi-purpose web-based data monitoring system. For more details, please look at the link(<https://github.com/odakahirokazu/HSQuicklook>)

- pymongo

  Module for handle mongoDB (Optional).
  
- sounddevice
  
  Module to warn you in case of error (Optional)
  
## How to Use

### pyGL840

Please see the example code of Run_GL840.py

### Warning

If you use sound/slack notification, this feature is separeted from Run_GL840.py. So, you need to run GL840Notification.py.
