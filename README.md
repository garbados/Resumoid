# RESUMOID

## Let Work Speak

You didn't learn everything you know on the job, so why let your resume imply that? Use Resumoid to build a portfolio of your skills and abilities, and let your talents speak for you.

The best and the brightest don't spend their time practicing resume writing. They spend it honing what make them great. Find them on their merits. Let their work speak for itself.

## Installation

Get the repo

    git clone git@github.com:garbados/Resumoid.git

Install python requirements

    virtualenv venv --no-site-packages
    source venv/bin/activate
    pip install -r requirements.txt

Resumoid uses `flask-assets`, which requires [node.js](http://nodejs.org/#)

Install more requirements after installing node for your system

    git submodule init
    git submodule update

Create config.settings

    touch config/settings.py

That should be it! Email me at garbados@gmail.com if it isn't.

## Running Resumoid

`python app.py run`

## Authentication

Users should be able to authenticate easily using whatever service they feel comfortable with. However, this is a convenience and thus the MVP will use BrowserID to manage user authentication. Protocols like OpenID will be integrated after the MVP.

### User Model

Thanks to BrowserID, the user model consists only of an email field. Password encryption and verification occurs off-site.

Implementing persistent login will occur after the MVP.

### User Privileges

This section will be implemented after the MVP.

There are two types of users:

1. User: basic users can view all public data, and edit data that belongs to them.
2. Admin: administrators can view and edit all data, public and private.

### Storing Sensitive Data

For security purposes, no information on the site should be sensitive from a legal perspective if it gets out. Under no circumstances should we have, store, or be anywhere close to:

* SSN
* Passwords

Under even the most dire circumstances, such as if an attacker acquired the entire database, they would only have access to information that is already public.

## Portfolio

When employers and recruiters assess talent, they're trying to answer two fundamental questions: 

1. Can the candidate do the work we need done? 
2. Will the candidate enrich our team?

Portfolios display examples of your work, making it much easier to answer #1 than with traditional resumes. Resumoid allows users to add custom sections to their portfolios, such as *Goals* or *Needs* that give more insight into your character and personality, helping to answer #2. You can also style your portfolio with custom HTML / CSS templates. For safety reasons, <script></script> tags will be stripped, though custom templates can use HTML5 attributes to hook into Twitter Bootstrap Javascript components such as dropdowns and image carousels.

Resumoid portfolios reside at [resumoid url]/p/[portfolio id]

### User Stories

In administering their portfolio, a user can:

1. Add, remove, and reorder sections, and change their content
2. Add and remove work examples, and change their content
3. Change the portfolio's header and subheader
4. Add, remove, and change links to external sites like blogs and the like
5. Change the portfolio's HTML and CSS

### Models

The portfolio consists of models within models, wheels within wheels, spinning their webs and secrets... aherm, I mean, let's continue:

#### Portfolio

* References a User, who has the power to edit the portfolio.
* Has a header, subheader, HTML template, and CSS template
* Has many sections
* Has many work samples
* Has many links

#### Section

* References a Portfolio
* Has a title, body, creation date, and list of dates upon which it was updated
* The body is rendered in markdown
* Has a way of being arbitrarily ordered by the user relative to other Sections with this Portfolio

#### Work Sample

* References a Portfolio
* Has a title, body, tags, creation date, and list of dates upon which it was updated
* The body is rendered in markdown
* May reference a Question, which the Work Sample answers.
* If the Work Sample has a Question, it inherits the Question's tags
* Ordered on the Portfolio by creation date

#### Link

* References a Portfolio
* Has a title and url
* Has a way of being arbitrarily ordered by the user relative to other Links with this Portfolio

#### HTML Template

* Jinja2 template, with access to the user's portfolio. Scrub for JS and validate, but otherwise safe.
* Take care to strip out sensitive variables and filters from the available context!

#### CSS Template

* Static text

## Opportunity

## Hiring

## Recommendation
