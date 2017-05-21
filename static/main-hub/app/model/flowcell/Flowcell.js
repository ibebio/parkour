Ext.define('MainHub.model.flowcell.Flowcell', {
    extend: 'MainHub.model.Base',

    fields: [{
            name: 'flowcellId',
            type: 'string'
        }, {
            name: 'flowcell',
            type: 'int'
        }, {
            name: 'pool',
            type: 'int'
        }, {
            name: 'laneId',
            type: 'int'
        }, {
            name: 'laneName',
            type: 'string'
        }, {
            name: 'poolName',
            type: 'string'
        }, {
            name: 'readLengthName',
            type: 'string'
        }, {
            name: 'sequencer',
            type: 'int'
        }, {
            name: 'sequencerName',
            type: 'string'
        },
        {
            name: 'equalRepresentation',
            type: 'string'
        },
        {
            name: 'loading_concentration',
            type: 'float',
            allowNull: true
        },
        {
            name: 'phix',
            type: 'float',
            allowNull: true
        }
    ]
});
