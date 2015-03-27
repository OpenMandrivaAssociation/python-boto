%define module boto

%define debug_package %{nil}

Name:           python-%{module}
Version:	2.35.2
Release:        1
License:        MIT
Summary:        Python interface to Amazon Web Services

Url:            http://code.google.com/p/boto/
Group:          Development/Python
Source0:	http://pypi.python.org/packages/source/b/boto/boto-%{version}.tar.gz
BuildRequires:  python-setuptools

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
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --root %{buildroot} --install-purelib=%{py_platsitedir}

%files 
%{py_platsitedir}/*
%{_bindir}/*
