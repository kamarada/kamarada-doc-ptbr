#
# spec file for package kamarada-doc-ptbr
#
# Copyright (c) 2014 Kamarada Project, Aracaju, Brazil.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://github.com/kamarada
#


Name:           kamarada-doc-ptbr
Version:        13.1
Release:        1
Summary:        Kamarada documentation and help files in Brazilian Portuguese
License:        GPL-2.0+
Group:          Documentation
Source0:        LICENSE
Url:            http://github.com/kamarada/kamarada-doc-ptbr
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Requires:       kde4-l10n-pt_BR-doc
Requires:       libreoffice-help-pt-BR


%description
Kamarada documentation and help files in Brazilian Portuguese


%prep
cp -a %{SOURCE0} COPYING


%build


%install


%files
%defattr(-,root,root)
%doc COPYING


%changelog
* Wed Sep 03 2014 kamaradalinux@gmail.com
- Initial draft
