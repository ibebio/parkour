Ext.define('MainHub.store.tables.libraries.SequencingRunConditions', {
    extend: 'Ext.data.Store',
    storeId: 'sequencingRunConditionsStore',

    requires: [
        'MainHub.model.tables.libraries.LibraryField'
    ],

    model: 'MainHub.model.tables.libraries.LibraryField',

    proxy: {
        type: 'ajax',
        url: 'get_sequencing_run_conditions/',
        timeout: 1000000,
        pageParam: false,   //to remove param "page"
        startParam: false,  //to remove param "start"
        limitParam: false,  //to remove param "limit"
        noCache: false,     //to remove param "_dc",
        reader: {
            type: 'json',
            rootProperty: 'data',
            successProperty: 'success'
        }
    },

    listeners: {
        load: function(store, records, success, operation) {
            if (!success) {
                var response = operation._response,
                    obj = Ext.JSON.decode(response.responseText);
                console.log('[ERROR]: get_sequencing_run_conditions(): ' + obj.error);
                console.log(response);
            }
        }
    }
});
