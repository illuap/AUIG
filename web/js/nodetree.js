
    var chart_config = {
        chart: {
            container: "#nodetree",

            animateOnInit: true,
            
            node: {
                collapsable: true
            },
            animation: {
                nodeAnimation: "easeOutBounce",
                nodeSpeed: 700,
                connectorsAnimation: "bounce",
                connectorsSpeed: 700
            }
        },
        nodeStructure: {
            text: {
                actionType: "FIND_AND_CLICK",
                START_DELAY: "Start Delay: " + 1.5,
                POST_DELAY: "POST Delay: " + 0.5,
            },
            image: "img/malory.png",
            children: [
                {
                    image: "img/lana.png",
                    collapsed: true,
                    children: [
                        {
                            text: {
                                actionType: "FIND_AND_CLICK",
                                START_DELAY: "Start Delay: " + 1.5,
                                POST_DELAY: "POST Delay: " + 0.5,
                            },
                            image: "img/figgs.png"
                        }
                    ]
                },
                {
                    image: "img/sterling.png",
                    childrenDropLevel: 1,
                    children: [
                        {
                            image: "img/woodhouse.png"
                        }
                    ]
                },
                {
                    pseudo: true,
                    children: [
                        {
                            image: "img/cheryl.png"
                        },
                        {
                            image: "img/pam.png"
                        }
                    ]
                }
            ]
        }
    };
