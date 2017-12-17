Ext.define('MainHub.view.invoicing.Invoicing', {
  extend: 'Ext.container.Container',
  xtype: 'invoicing',

  requires: [
    'MainHub.view.invoicing.BaseCostGrid',
    'MainHub.view.invoicing.InvoicingController'
  ],

  controller: 'invoicing',

  layout: {
    type: 'hbox',
    align: 'stretch'
  },

  items: [
    {
      xtype: 'grid',
      id: 'invoicing-grid',
      itemId: 'invoicing-grid',
      height: Ext.Element.getViewportHeight() - 64,
      padding: 15,
      flex: 1,

      viewConfig: {
        deferEmptyText: false,
        emptyText: '<h1 style="text-align:center;margin:75px">No items</h1>',
        stripeRows: false
      },

      header: {
        title: 'Invoicing',
        height: 56
      },

      store: 'Invoicing',

      sortableColumns: false,
      enableColumnMove: false,
      columns: {
        defaults: {
          minWidth: 200,
          flex: 1
        },
        items: [
          {
            text: 'Request',
            dataIndex: 'request'
          },
          {
            text: 'Cost Unit',
            dataIndex: 'cost_unit',
            renderer: 'listRenderer'
          },
          {
            text: 'Sequencer',
            dataIndex: 'sequencer',
            renderer: 'sequencerRenderer'
          },
          {
            text: 'Date + Flowcell ID',
            dataIndex: 'flowcell',
            renderer: 'listRenderer'
          },
          {
            text: 'Pool',
            dataIndex: 'pool',
            renderer: 'listRenderer'
          },
          {
            text: '%',
            dataIndex: 'percentage',
            renderer: 'percentageRenderer'
          },
          {
            text: 'Read Length',
            dataIndex: 'read_length',
            renderer: 'readLengthRenderer'
          },
          {
            text: '# of Libraries/Samples',
            dataIndex: 'num_libraries_samples',
            minWidth: 150
          },
          {
            text: 'Library Protocol',
            dataIndex: 'library_protocol',
            renderer: 'libraryProtocolRenderer'
          },
          {
            text: 'Fixed Costs',
            dataIndex: 'fixed_costs',
            renderer: Ext.util.Format.deMoney,
            minWidth: 130
          },
          {
            text: 'Sequencing Costs',
            dataIndex: 'sequencing_costs',
            renderer: Ext.util.Format.deMoney,
            minWidth: 130
          },
          {
            text: 'Preparation Costs',
            dataIndex: 'preparation_costs',
            renderer: Ext.util.Format.deMoney,
            minWidth: 130
          },
          {
            text: 'Variable Costs',
            dataIndex: 'variable_costs',
            renderer: Ext.util.Format.deMoney,
            minWidth: 130
          },
          {
            text: 'Total Costs',
            dataIndex: 'total_costs',
            renderer: Ext.util.Format.deMoney,
            minWidth: 130
          }
        ]
      },

      plugins: [
        {
          ptype: 'bufferedrenderer',
          trailingBufferZone: 100,
          leadingBufferZone: 100
        }
      ],

      dockedItems: [
        {
          xtype: 'toolbar',
          dock: 'top',
          items: [{
            xtype: 'combobox',
            itemId: 'billing-period-combobox',
            fieldLabel: 'Select Billing Period',
            store: 'BillingPeriods',
            queryMode: 'local',
            valueField: 'value',
            displayField: 'name',
            forceSelection: true,
            labelWidth: 130,
            width: 300
          }]
        }
      ]
    },
    {
      title: 'Costs',
      // headerPosition: 'right',
      padding: '15px 10px 15px 0',
      margin: '0 8px 0 0',
      autoScroll: true,
      height: Ext.Element.getViewportHeight() - 64,
      width: 350,

      collapsed: true,
      collapsible: true,
      collapseDirection: 'right',

      defaults: {
        border: 0
      },

      items: [
        {
          xtype: 'costgrid',
          itemId: 'fixed-costs-grid',
          configUrl: 'fixedcosts',
          title: 'Fixed Costs',
          store: 'FixedCosts'
        },
        {
          xtype: 'costgrid',
          itemId: 'preparation-costs-grid',
          configUrl: 'librarypreparationcosts',
          title: 'Preparation Costs',
          store: 'LibraryPreparationCosts'
        },
        {
          xtype: 'costgrid',
          itemId: 'sequencing-costs-grid',
          configUrl: 'sequencingcosts',
          title: 'Sequencing Costs',
          store: 'SequencingCosts'
        }
      ]
    }
  ]
});