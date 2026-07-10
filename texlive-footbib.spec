%global tl_name footbib
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.7
Release:	%{tl_revision}.1
Summary:	Bibliographic references as footnotes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/footbib
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/footbib.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/footbib.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/footbib.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package makes bibliographic references appear as footnotes. It
defines a command \footcite which is similar to the LaTeX \cite command
but the references cited in this way appear at the bottom of the pages.
This 'foot bibliography' does not conflict with the standard one and
both may exist simultaneously in a document. The command \cite may still
be used to produce the standard bibliography. The foot bibliography uses
its own style and bibliographic database which may be specified
independently of the standard one. Any standard bibliography style may
be used.

