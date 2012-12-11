%define module boto

Name:           python-%{module}
Version:	2.2.2
Release:        1
License:        MIT
Summary:        Python interface to Amazon Web Services
Url:            http://code.google.com/p/boto/
Group:          Development/Python
Source0:	http://boto.googlecode.com/files/%{module}-%{version}.tar.gz
BuildRequires:  python-setuptools
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
%setup -q -n %{module}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitearch}

%files 
%{python_sitearch}/*
%{_bindir}/*




%changelog
* Sat Feb 18 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.2.2-1
+ Revision: 777032
- version update 2.2.2

* Wed Jun 08 2011 Antoine Ginies <aginies@mandriva.com> 2.0-1
+ Revision: 683242
- import python-boto

