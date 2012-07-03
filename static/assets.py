from flask.ext.assets import Environment, Bundle

assets = Environment()

js = Bundle('jquery.js',
            'include.js',
            'less.js',
            'auth.js',
            'backbone.js',
            'handlebars.js',
            filters='jsmin',
            output='bundle.js')
            
less = Bundle('bootstrap/less/bootstrap.less',
              'myless.less',
              # filters='less', 
              output='bundle.less',
              debug=False)

bundles = [['js', js], ['less', less]]

for bundle in bundles:
    asset.register(*bundle)
