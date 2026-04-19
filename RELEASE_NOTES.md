# Release Notes

## v1.1

### Features

- Added **internationalisation support**: The script now detects the system locale and displays a localised ASCII art and message.
  - English: "It does everything and the kitchen sink."
  - Spanish: "Lo hace todo menos hablar."
  - French: "Il fait tout sauf le café."
  - Default: "It does everything but make coffee."

### Improvements

- Added locale detection using the `$LANG` environment variable.
- Updated ASCII art for each supported language.

---

## v1.0

### Features

- Initial release of `systemd-coffeed`.
- Displays a default ASCII art of a coffee machine.
- Supports version flag (`-v` or `--version`) to display the script version.

### Usage

```bash
./systemd-coffeed.sh [OPTIONS]
```

- `-v, --version`: Display the script version.
