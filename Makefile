PREFIX = /usr
BINDIR = $(PREFIX)/bin
SERVICEDIR = $(PREFIX)/lib/systemd/system

BINARY = systemd-coffeed
SERVICE = systemd-coffeed.service

.PHONY: install uninstall

install:
	install -m 755 -v $(BINARY) $(BINDIR)/
	install -m 644 -v $(SERVICE) $(SERVICEDIR)/
	systemctl daemon-reload
	@echo "Install OK"

uninstall:
	rm -f $(BINDIR)/$(BINARY)
	rm -f $(SERVICEDIR)/$(SERVICE)
	systemctl daemon-reload
	@echo "Uninstall OK"
