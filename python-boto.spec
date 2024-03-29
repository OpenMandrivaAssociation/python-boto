%define module boto

%define debug_package %{nil}

Name:           python-%{module}
Version:	2.49.0
Release:	3
License:        MIT
Summary:        Python interface to Amazon Web Services

Url:            https://pypi.org/project/boto/
Group:          Development/Python
Source0:	https://files.pythonhosted.org/packages/c8/af/54a920ff4255664f5d238b5aebd8eedf7a07c7a5e71e27afcfe840b82f51/%{module}-%{version}.tar.gz
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
%autosetup -n %{module}-%{version} -p1

%build
%set_build_flags
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --root %{buildroot} --install-purelib=%{py_platsitedir}

%files 
%{py_platsitedir}/*
%{_bindir}/*
