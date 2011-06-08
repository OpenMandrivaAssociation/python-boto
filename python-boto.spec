%define extraver rc1
%define module boto

Name:           python-%{module}
Version:	2.0
Release:        %mkrel 1
License:        MIT
Summary:        Python interface to Amazon Web Services
Url:            http://code.google.com/p/boto/
Group:          Development/Python
Source:         %{module}-%{version}%{extraver}.tar.gz
BuildRequires:  python-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Buildarch:	noarch

%description
An integrated interface to current and future infrastructural
services offered by Amazon Web Services. Currently, this includes:
    * Simple Storage Service (S3)
    * SimpleQueue Service (SQS)
    * Elastic Compute Cloud (EC2)
    * Mechanical Turk
    * SimpleDB
    * CloudFront
    * CloudWatch
    * AutoScale
    * Elastic Load Balancer (ELB)
    * Virtual Private Cloud (VPC)
    * Elastic Map Reduce (EMR)
    * Relational Data Service (RDS)
    * Simple Notification Server (SNS)
    * Google Storage
    * Identity and Access Management (IAM)
    * Route53 DNS Service (route53) 

%prep
%setup -q -n %{module}-%{version}%{extraver}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitearch}

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{python_sitearch}/*
%{_bindir}/*


