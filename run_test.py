import pytest

pytest.main(['--cov=utils', '--cov=main', '--cov-report=term', 
             '--cov-report=html:coverage_report', '--html=test_report.html',
             'tests'])
