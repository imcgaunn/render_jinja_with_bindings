# What Is This?

`rendertempl` is a script that is useful for when you just want to
see what a Jinja2 template will look like when it is rendered
with particular bindings for template variables without having to instantiate
a full web django webapp or run an ansible playbook.


## How Do I Use It?

```
usage: rendertempl [-h] [--file FILE | --directory DIRECTORY] tmpl

render a jinja2 template with the specified variable bindings

positional arguments:
  tmpl                  the template to render

optional arguments:
  -h, --help            show this help message and exit
  --file FILE, -f FILE
  --directory DIRECTORY, -d DIRECTORY
                        an optional directory of yaml files containing
                        bindings. The files will be concatenated in
                        lexicographical order

```

