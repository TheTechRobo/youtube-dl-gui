deb:
	@echo Writing to DEBFILE...
	cd $HOME/youtube-dl-gui-1.3;take build;cp -r ../debian DEBIAN; \
		cp -r ../tree .;dpkg-deb --build tree

clean:
	@echo Removing BUILD directory ...
	rm -RI $HOME/youtube-dl-gui-1.3/build

all:
	@echo Please say something\!\!
