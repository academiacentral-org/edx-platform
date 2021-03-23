mooc.academiacentral.org
------------------------
.. image:: https://img.shields.io/badge/hack.d-Lawrence%20McDaniel-orange.svg
     :target: https://lawrencemcdaniel.com
     :alt: Hack.d Lawrence McDaniel

This is the edx-platform fork for the Open edX installation `mooc.academiacentral.org <https://mooc.academiacentral.org>`_.
Note that the edxapp servers for mooc.academiacentral.org are not configured to automatically use this fork during platform updates. 
For more information on upgrading the Open edX platform see:

.. _Upgrading Open edX: https://blog.lawrencemcdaniel.com/upgrading-open-edx/
.. _How Stanford Runs Its Own Fork: https://open.edx.org/blog/how-stanford-runs-its-own-fork/



Change Log
----------
- McDaniel mar-2021: 
1. Gradebook name column was modified. `See this commit <https://github.com/academiacentral-org/edx-platform/tree/990f65ee419257afe101ec28827d6b639e9cb7d5>`_. This changes the grade book "username" column to instead be "Last Name, First Name".
2. Base email template (set logo, etc.) /edx/app/edxapp/edx-platform/openedx/core/djangoapps/ace_common/templates/ace_common/edx_ace/common/base_body.html
3. Modify enrollment email notification. add University name. add custom sentence about intro video. /edx/app/edxapp/edx-platform/lms/templates/instructor/edx_ace/allowedenroll/email/body.html
4. prevent ENABLE_MKTG_SITE from 
   - redirecting the home page: /edx/app/edxapp/edx-platform/lms/djangoapps/branding/views.py
   - disabling course discovery page: /edx/app/edxapp/edx-platform/lms/djangoapps/branding/views.py
   - disabling course about page: /edx/app/edxapp/edx-platform/lms/djangoapps/courseware/views/views.py
   - /edx/app/edxapp/edx-platform/lms/djangoapps/instructor/enrollment.py
5. Fix "Sign in" link on email base template: /edx/app/edxapp/edx-platform/openedx/core/djangoapps/ace_common/templates/ace_common/edx_ace/common/base_body.html
6. set min_price to zero for verified course mode: /edx/app/edxapp/edx-platform/lms/envs/common.py
   change COURSE_MODE_DEFAULTS from 'Audit' to 'Honor'

Open edX
--------
This is the core repository of the Open edX software. It includes the LMS
(student-facing, delivering courseware), and Studio (course authoring)
components.

Installation
------------

Installing and running an Open edX instance is not simple.  We strongly
recommend that you use a service provider to run the software for you.  They
have free trials that make it easy to get started:
https://openedx.org/get-started/

If you will be modifying edx-platform code, the `Open edX Developer Stack`_ is
a Docker-based development environment.

If you want to run your own Open edX server and have the technical skills to do
so, `Open edX Installation Options`_ explains your options.

.. _Open edX Developer Stack: https://github.com/edx/devstack
.. _Open edX Installation Options:  https://openedx.atlassian.net/wiki/spaces/OpenOPS/pages/60227779/Open+edX+Installation+Options

License
-------

The code in this repository is licensed under version 3 of the AGPL
unless otherwise noted. Please see the `LICENSE`_ file for details.

.. _LICENSE: https://github.com/edx/edx-platform/blob/master/LICENSE


More about Open edX
-------------------

See the `Open edX site`_ to learn more about the Open edX world. You can find
information about hosting, extending, and contributing to Open edX software. In
addition, the Open edX site provides product announcements, the Open edX blog,
and other rich community resources.

.. _Open edX site: https://openedx.org

Documentation
-------------

Documentation can be found at https://docs.edx.org.


Getting Help
------------

If you're having trouble, we have discussion forums at
https://discuss.openedx.org where you can connect with others in the community.

Our real-time conversations are on Slack. You can request a `Slack
invitation`_, then join our `community Slack team`_.

For more information about these options, see the `Getting Help`_ page.

.. _Slack invitation: https://openedx-slack-invite.herokuapp.com/
.. _community Slack team: http://openedx.slack.com/
.. _Getting Help: https://openedx.org/getting-help


Issue Tracker
-------------

We use JIRA for our issue tracker, not GitHub issues. You can search
`previously reported issues`_.  If you need to report a problem,
please make a free account on our JIRA and `create a new issue`_.

.. _previously reported issues: https://openedx.atlassian.net/projects/CRI/issues
.. _create a new issue: https://openedx.atlassian.net/secure/CreateIssue.jspa?issuetype=1&pid=11900


How to Contribute
-----------------

Contributions are welcome! The first step is to submit a signed
`individual contributor agreement`_.  See our `CONTRIBUTING`_ file for more
information – it also contains guidelines for how to maintain high code
quality, which will make your contribution more likely to be accepted.


Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email
security@edx.org.

.. _individual contributor agreement: https://openedx.org/cla
.. _CONTRIBUTING: https://github.com/edx/edx-platform/blob/master/CONTRIBUTING.rst
