#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-drc
Version  : 3.0.1
Release  : 24
URL      : https://cran.r-project.org/src/contrib/drc_3.0-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/drc_3.0-1.tar.gz
Summary  : Analysis of Dose-Response Curves
Group    : Development/Tools
License  : GPL-2.0
Requires: R-TH.data
Requires: R-car
Requires: R-gtools
Requires: R-multcomp
Requires: R-plotrix
Requires: R-scales
BuildRequires : R-TH.data
BuildRequires : R-car
BuildRequires : R-gtools
BuildRequires : R-multcomp
BuildRequires : R-plotrix
BuildRequires : R-scales
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n drc

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569268090

%install
export SOURCE_DATE_EPOCH=1569268090
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library drc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library drc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library drc
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc drc || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/drc/CITATION
/usr/lib64/R/library/drc/DESCRIPTION
/usr/lib64/R/library/drc/INDEX
/usr/lib64/R/library/drc/LICENCE
/usr/lib64/R/library/drc/Meta/Rd.rds
/usr/lib64/R/library/drc/Meta/data.rds
/usr/lib64/R/library/drc/Meta/features.rds
/usr/lib64/R/library/drc/Meta/hsearch.rds
/usr/lib64/R/library/drc/Meta/links.rds
/usr/lib64/R/library/drc/Meta/nsInfo.rds
/usr/lib64/R/library/drc/Meta/package.rds
/usr/lib64/R/library/drc/NAMESPACE
/usr/lib64/R/library/drc/NEWS
/usr/lib64/R/library/drc/R/drc
/usr/lib64/R/library/drc/R/drc.rdb
/usr/lib64/R/library/drc/R/drc.rdx
/usr/lib64/R/library/drc/data/Rdata.rdb
/usr/lib64/R/library/drc/data/Rdata.rds
/usr/lib64/R/library/drc/data/Rdata.rdx
/usr/lib64/R/library/drc/help/AnIndex
/usr/lib64/R/library/drc/help/aliases.rds
/usr/lib64/R/library/drc/help/drc.rdb
/usr/lib64/R/library/drc/help/drc.rdx
/usr/lib64/R/library/drc/help/paths.rds
/usr/lib64/R/library/drc/html/00Index.html
/usr/lib64/R/library/drc/html/R.css
/usr/lib64/R/library/drc/tests/test1.R
/usr/lib64/R/library/drc/tests/test1.data1.txt
/usr/lib64/R/library/drc/tests/test1.w1.txt
/usr/lib64/R/library/drc/tests/test2.R
/usr/lib64/R/library/drc/tests/test2.redroot_dose.csv
/usr/lib64/R/library/drc/tests/test3.R
