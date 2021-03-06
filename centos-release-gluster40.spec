%global altarch 0
%if ( 0%{?centos} >= 7 )
%ifnarch x86_64
# altarch is only available for CentOS-7, non c86_64
%global altarch 1
%endif
%endif

Summary: Gluster 4.0 (Short Term Stable) packages from the CentOS Storage SIG repository
Name: centos-release-gluster40
Version: 1.0
Release: 3%{?dist}
License: GPLv2
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
Source0: CentOS-Gluster-4.0.repo

# This provides the public key to verify the RPMs
Requires: centos-release-storage-common

# Users can install centos-release-gluster to get the latest, but we do not
# want to have 4.0 (Short Term Stable) to be selected when users do install
# the virtual centos-release-gluster package.
#
# If users want to test other projects with a centos-release-gluster
# dependency, they will need to install centos-release-gluster313 or similar in
# addition to centos-release-gluster40
#
#Provides: centos-release-gluster = 4.0
#Conflicts: centos-release-gluster < 4.0
#Obsoletes: centos-release-gluster < 4.0

%description
yum configuration for Gluster 4.0 packages from the CentOS Storage SIG.
Gluster 4.0 is a Short Term Stable release and will receive updates for only 3
months (until the next Gluster release is available). For more details about
the Long Term Stable and Short Term Stable release schedule, see
https://www.gluster.org/community/release-schedule

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Gluster-4.0.repo
%if %{altarch}
sed -i -e "s,@BASEURL@,http://mirror.centos.org/altarch," %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Gluster-4.0.repo
%else
sed -i -e "s,@BASEURL@,http://mirror.centos.org/centos," %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Gluster-4.0.repo
%endif

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-Gluster-4.0.repo

%changelog
* Thu Mar 15 2018 Niels de Vos <ndevos@redhat.com> - 1.0-3
- Fix altarch detection for .el6/i686

* Thu Mar 15 2018 Niels de Vos <ndevos@redhat.com> - 1.0-2
- Correct the repository URL

* Wed Mar 7 2018 Niels de Vos <ndevos@redhat.com> - 1.0-1
- Disable centos-gluster40-test, enable centos-gluster40 repo

* Fri Jan 12 2018 Niels de Vos <ndevos@redhat.com> - 0.9-1
- Initial version based on centos-release-gluster313
- Only the centos-gluster40-test repo is enabled during Beta
