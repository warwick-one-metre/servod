RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

GIT_VERSION = $(shell git name-rev --name-only --tags --no-undefined HEAD 2>/dev/null || echo git-`git rev-parse --short HEAD`)
SERVER_VERSION=$(shell awk '/Version:/ { print $$2; }' observatory-servo-server.spec)

all:
	mkdir -p build
	cp servod servod.bak
	awk '{sub("SOFTWARE_VERSION = .*$$","SOFTWARE_VERSION = \"$(SERVER_VERSION) ($(GIT_VERSION))\""); print $0}' servod.bak > servod
	${RPMBUILD} -ba observatory-servo-server.spec
	${RPMBUILD} -ba observatory-servo-client.spec
	${RPMBUILD} -ba python3-warwick-observatory-servo.spec
	${RPMBUILD} -ba onemetre-servo-data.spec
	mv build/noarch/*.rpm .
	rm -rf build
	mv servod.bak servod
