# revision 30267
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-babel-finnish
Version:	20131013
Release:	6
Summary:	TeXLive babel-finnish package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-finnish.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-finnish.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-finnish.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive babel-finnish package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-finnish/finnish.ldf
%doc %{_texmfdistdir}/doc/generic/babel-finnish/finnish.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-finnish/finnish.dtx
%doc %{_texmfdistdir}/source/generic/babel-finnish/finnish.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
