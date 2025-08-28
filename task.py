import os
import jinja2
import requests

template_loader = jinja2.FileSystemLoader("templates")
template_env = jinja2.Environment(loader=template_loader)

def render_template(template_name, **context):
    return template_env.get_template(template_name).render(**context)

def send_simple_message(to, subject, body, html): 
  	return requests.post(
  		"https://api.mailgun.net/v3/sandbox2ba929e719c8481db30714b19fa8e88d.mailgun.org/messages",
  		auth=("api", os.getenv('API_KEY', 'API_KEY')),
  		data={"from": "Mailgun Sandbox <postmaster@sandbox2ba929e719c8481db30714b19fa8e88d.mailgun.org>",
			"to": f"User <{to}>",
  			"subject": subject,
  			"text": body,
            "html": html
            }
        )

def send_welcome_email(email, username): 
	return send_simple_message(
		to=email,
		subject="Welcome to our service!",
		body=f"Hello {username}, thank you for registering.",
		html=render_template("/mail/action.html", username=username)
	)