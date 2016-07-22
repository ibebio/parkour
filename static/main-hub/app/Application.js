/**
 * The main application class. An instance of this class is created by app.js when it
 * calls Ext.application(). This is the ideal place to handle application launch and
 * initialization details.
 */
Ext.Loader.setConfig({
    enabled: true,
    paths: {
        'Ext.ux': 'static/main-hub/ext/packages/ux/classic/src/'
    }
});

Ext.define('MainHub.Application', {
    extend: 'Ext.app.Application',

    name: 'MainHub',

    appFolder: '/static/main-hub/app',

    stores: [
      'NavigationTree',
      'tables.researchers.Researchers',
      'tables.researchers.PrincipalInvestigators',
      'tables.researchers.Organizations',
      'tables.researchers.CostUnits',
      'Requests'
    ],

    requires: [
        'Ext.ux.ToastMessage'
    ],

    launch: function () {
        // TODO - Launch the application
    },

    onAppUpdate: function () {
        Ext.Msg.confirm('Application Update', 'This application has an update, reload?',
            function (choice) {
                if (choice === 'yes') {
                    window.location.reload();
                }
            }
        );
    }
});
