Name:		texlive-footbib
Version:	17115
Release:	2
Summary:	Bibliographic references as footnotes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/footbib
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footbib.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footbib.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footbib.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package makes bibliographic references appear as footnotes.
It defines a command \footcite which is similar to the LaTeX
\cite command but the references cited in this way appear at
the bottom of the pages. This 'foot bibliography' does not
conflict with the standard one and both may exist
simultaneously in a document. The command \cite may still be
used to produce the standard bibliography. The foot
bibliography uses its own style and bibliographic database
which may be specified independently of the standard one. Any
standard bibliography style may be used.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/footbib/footbib.sty
%doc %{_texmfdistdir}/doc/latex/footbib/README
%doc %{_texmfdistdir}/doc/latex/footbib/footbib.pdf
#- source
%doc %{_texmfdistdir}/source/latex/footbib/footbib.dtx
%doc %{_texmfdistdir}/source/latex/footbib/footbib.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
