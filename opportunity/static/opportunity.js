$(function() {
        var GenericView = Backbone.View.extend({
            initialize: function(data) {
                if (this.model) {
                    _.bindAll(this, 'render');
                    this.model.bind('change', this.render, this);
                } else if (this.collection) {
                    this.collection.bind('add', this.addOne, this);
                    this.collection.bind('all', this.render, this);
                }
            },
            addOne : function(obj) {
                var view = new GenericView({ model : obj });
                this.$el.append(view.render().el);
            },

            render: function() {
                this.$el.html(this.template(this.model.toJSON()));
                return this;
            },
        });

        var Group = Backbone.Model.extend({
            url : '/api/group/',
        });

        var GroupList = Backbone.Collection.extend({
            model : Group,
        });

        var Router = Backbone.Router.extend({
            routes : {
                "/groups" : "group_list",
                "/group/:id" : "group_detail",
                "/opportunities" : "opportunity_list",
                "/opportunity/:id" : "opportunity_detail",
                "/questions" : "question_list",
                "/question/:id" : "question_detail",
                "/answers" : "answer_list",
                "/answer/:id" : "answer_detail",
            },

            group_list : function() {},
            group_detail : function() {},
            opportunity_list : function() {},
            opportunity_detail : function() {},
            question_list : function() {},
            question_detail : function() {},
            answer_list : function() {},
            answer_detail : function() {},
            default : function(path) {
                var template = path.substr(1);
                if (template === ' ') { template = 'base'; }
                ui.display(path, template);
            },
        });

        Backbone.history.start();
});
