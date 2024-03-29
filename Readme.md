### History
* 04-Mar-2024: (git commit: 6e01aef) Simplest example of simple django (tinyapp) with htmx with animation, __145 lines of code__
* 06-Mar-2024: (git commit: 41244f4) Deployed to ec2 with sample data using systemd, nginx, gunicorn, __159 lines of code__
* To Do: pull live data from REST API and display with htmx

### Run this app
```
django-admin runserver --pythonpath=. --settings=tinyapp
```

### References

* [https://dev.to/johntellsall/fast-web-minimal-django-p17](https://dev.to/johntellsall/fast-web-minimal-django-p17)
```
    django-admin runserver --pythonpath=. --settings=tinyapp
```

* [https://github.com/chriswedgwood/django-htmx-examples/tree/main/django_htmx_examples](https://github.com/chriswedgwood/django-htmx-examples/tree/main/django_htmx_examples)
* [https://dev.to/arthurobo/django-htmx-load-more-objects-3jg3](https://dev.to/arthurobo/django-htmx-load-more-objects-3jg3):
 _Bootstrap CSS styling from this project_

* [https://htmx.org/examples/animations/](https://htmx.org/examples/animations/)
* [https://htmx.org/attributes/hx-trigger/](https://htmx.org/attributes/hx-trigger/)
* [https://htmx.org/examples/lazy-load/](https://htmx.org/examples/lazy-load/)
* [https://htmx.org/attributes/hx-swap/](https://htmx.org/attributes/hx-swap/)
* [https://hypermedia.systems/deep-htmx/](https://hypermedia.systems/deep-htmx/)
* [https://stackoverflow.com/questions/9629346/difference-between-css3-transitions-ease-in-and-ease-out](https://stackoverflow.com/questions/9629346/difference-between-css3-transitions-ease-in-and-ease-out)
* [https://livebook.manning.com/book/django-in-action/chapter-12/v-6/14](https://livebook.manning.com/book/django-in-action/chapter-12/v-6/14)

### Deployed: 06-Mar-2024: (git commit: 41244f4)
* Installed on ec2 with this [ansible playbook](https://github.com/johnedstone/ansible-postgres-nginx-django) using these commands:
```
ansible-playbook --tags gunicorn-setup,letsencrypt --flush-cache --diff -i inventory.ini playbook.yaml
```

* Added wsgi.py and change running to `gunicorn --env DJANGO_SETTINGS_MODULE=tinyapp wsgi`, updated systemd files and set `INSTALL_SYSTEMD_FILES: false` in `ansible_private_vars.yaml`
