deb:
	make clean
	@echo Writing to DEBFILE...
	cd /home/thetechrobo/youtube-dl-gui-1.3;mkdir build;cd build; cp -r ../tree .; \
		cp -r ../debian tree/DEBIAN; \
		dpkg-deb --build tree

clean:
	@echo Removing BUILD directory ...
	rm -RI /home/thetechrobo/youtube-dl-gui-1.3/build

all:
	@echo Please say something\!\!
