deb:
	make clean
	@echo Writing to DEBFILE...
	cd /home/thetechrobo/youtube-dl-gui-1.3;mkdir build;cd build; cp -r ../tree .; \
		cp -r ../debian tree/DEBIAN; \
		dpkg-deb --build tree; \
		mv tree.deb youtube-dl-gui.deb
	@echo Done ! Please take your debfile.

clean:
	@echo Removing BUILD directory ...
	rm -fRIv /home/thetechrobo/youtube-dl-gui-1.3/build || echo "Couldn't delete build folder"
	sleep 2

all:
	@echo Please say something\!\!
