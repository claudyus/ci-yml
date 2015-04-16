.ci.yml parser/runner for Gitlab-CI
===================================

.. image:: https://travis-ci.org/claudyus/ci-yml.svg?branch=master
    :target: https://travis-ci.org/claudyus/ci-yml

The ci-yml utilities read the local .ci.yml file and run a series of action grouped under jobs.

The .ci.yml file may define a `deploy` job and a list of other parallel jobs that can be assigned 1-to-1 with the gitlab-CI `test` jobs.

This is a .ci.yml example file::

  prepare:
    - <shell command>
    - <shell command>
  jobs:
    <jobname>:
      - <shell command>
    <jobname>:
      - <shell command>
  deploy:
    - <shell command>
    - <shell command>

In the example below we have two jobs, a `prepare` job used to install additional package::

  prepare:
    - pip install pyyaml

  jobs:
    test1:
      - python ./test1.py
    build_doc:
      - make doc

The commands inside `prepare` block are executed before that any other jobs is executed and the errors are ignored.

Following the example above you should configure two test jobs in you gitlab-ci instance and just call::

  ci-yml test1 

and::

  ci-yml build_doc

respectively. If you have also a deploy job you should also setup the gitlab-ci deploy job with the only command::

  ci-yml deploy

Environment variables
^^^^^^^^^^^^^^^^^^^^^^^

ci-yml extend the env variables with the follows:

  - CI_YML_JOB

To see the gitlab environment variables see https://gitlab.com/gitlab-org/gitlab-ci/tree/master/doc/examples#environmental-variables
Travis envs doc are available at http://docs.travis-ci.com/user/environment-variables/

ci-yml and travis
^^^^^^^^^^^^^^^^^

This project was intended to supply a job configuration method to gitlab-ci that don't have any one atm, otherwise it could be useful also in others use cases.

You can use ci-yml locally during developing and you can also call it inside `.travis.yml`, see the local travis config file for info.
