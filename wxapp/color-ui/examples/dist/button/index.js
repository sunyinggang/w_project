Component({
    externalClasses: ['c-class'],
    behaviors: [],
    // 属性定义（详情参见下文）
    properties: {
        size: {
            type: String,
            value: 'medium',
            options: ['sm', 'lg', 'medium']
        },
        bg: {
            type: String,
            value: 'blue'
        },
        shape: {
            type: String,
            value: 'square'
        },
        shadow: {
            type: Boolean,
            value: false,
        },
        line: {
            type: Boolean,
            value: false,
        }
    },

    methods: {}

});