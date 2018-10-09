dbus-monitor --session "type='signal',interface='com.ubuntu.Upstart0_6'" | \
(
  while true; do
    read X
	echo $X
    if echo $X | grep "desktop-lock" &> /dev/null; then
      SCREEN_LOCKED;
    elif echo $X | grep "desktop-unlock" &> /dev/null; then
      SCREEN_UNLOCKED;
    fi
  done
)
