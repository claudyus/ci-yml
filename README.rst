.ci.yml parser for gitlab-ci
=============================

The ci-yml utilities read the local .ci.yml file and run a series of action grouped under jobs.

The .ci.yml file may define a `deploy` job and a list of other parallel jobs that can be assigned 1-to-1 with the gitlab-CI `test` jobs.

This is a .ci.yml example file::

  prepare:
    - <shell command>
    - <shell command>
  test:
    <jobname>:
      - <shell command>
    <jobname>:
      - <shell command>
  deploy:
    - <shell command>
    - <shell command>

For example a series of test that require the installation of additional package could be::

  prepare:
    - pip install pyyaml

  test:
    test1:
      - python ./test1.py
    build_doc:
      - make doc

In the example above the commands inside `prepare` block are executed before that any other jobs is executed.

Following this example you should configure two test jobs in you gitlab-ci instance and just call::

  ci-yml test1 

and::

  ci-yml build_doc

respectively. If you have also e deploy job you should also setup the gitlab-ci deploy job with the only command::

  ci-yml deploy 