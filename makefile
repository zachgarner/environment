all: clean dist

clean:
	rm -rf build dist

dist:
	mkdir -p build/BUILD build/RPMS build/SRPMS
	rpmbuild --define "date `date +'%Y%m%d'`" \
            --define "time `date +'%H%M'`" \
            --define '_topdir build' -ba *.spec

	mkdir dist
	ln `find build -name \*.rpm` dist/

publish: clean dist
	cp -v dist/*.rpm /srv/yum/
	createrepo /srv/yum
