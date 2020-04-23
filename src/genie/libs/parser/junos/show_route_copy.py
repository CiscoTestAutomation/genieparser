class ShowRouteSummarySchema(MetaParser):
    """ Schema for:
            * show route summary
    """
    # schema = {
    #     Optional("@xmlns:junos"): str,
    #     "route-summary-information": {
    #         Optional("@xmlns"): str,
    #         "as-number": str,
    #         "route-table": [
    #             {
    #                 "active-route-count": str,
    #                 "destination-count": str,
    #                 "hidden-route-count": str,
    #                 "holddown-route-count": str,
    #                 "protocols": [
    #                     {
    #                         "active-route-count": str,
    #                         "protocol-name": str,
    #                         "protocol-route-count": str
    #                     }
    #                 ],
    #                 "table-name": str,
    #                 "total-route-count": str
    #             }
    #         ],
    #         "router-id": str
    #     }
    # }

    def validate_route_table_list(value):
        # Pass route-table list of dict in value
        if not isinstance(value, list):
            raise SchemaTypeError('route-table is not a list')
        def validate_protocols_list(value):
            # Pass protocols list of dict in value
            if not isinstance(value, list):
                raise SchemaTypeError('protocols is not a list')
            # Create protocols Schema
            protocols_schema = Schema({
                "active-route-count": str,
                "protocol-name": str,
                "protocol-route-count": str
            })
            # Validate each dictionary in list
            for item in value:
                protocols_schema.validate(item)
            return value
        # Create route-table Schema
        route_table_schema = Schema({
            "active-route-count": str,
            "destination-count": str,
            "hidden-route-count": str,
            "holddown-route-count": str,
            "protocols": Use(validate_protocols_list),
            "table-name": str,
            "total-route-count": str
        })
        # Validate each dictionary in list
        for item in value:
            route_table_schema.validate(item)
        return value

    # Main Schema
    schema = {
        Optional("@xmlns:junos"): str,
        "route-summary-information": {
            Optional("@xmlns"): str,
            "as-number": str,
            "route-table": Use(validate_route_table_list),
            "router-id": str
        }
    }

class ShowRouteSummary(ShowRouteSummarySchema):
    """ Parser for:
            * show route summary
    """
    cli_command = 'show route summary'
    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        ret_dict = {}

        # Autonomous system number: 65171
        p1 = re.compile(r'^Autonomous +system +number: +(?P<as_number>\d+)$')

        # Router ID: 111.87.5.252
        p2 = re.compile(r'^Router +ID: +(?P<router_id>\S+)$')

        # inet.0: 929 destinations, 1615 routes (929 active, 0 holddown, 0 hidden)
        p3 = re.compile(r'^(?P<table_name>\S+): +(?P<destination_count>\d+) +'
                r'destinations, +(?P<total_route_count>\d+) +routes +'
                r'\((?P<active_route_count>\d+) +active, +(?P<holddown_route_count>\d+) +'
                r'holddown, +(?P<hidden_route_count>\d+) +hidden\)$')
        
        #  Direct:      6 routes,      6 active
        p4 = re.compile(r'^(?P<protocol_name>\S+): +(?P<protocol_route_count>\d+) +'
                r'routes, +(?P<active_route_count>\d+) +\w+$')

        for line in out.splitlines():
            line = line.strip()

            # Autonomous system number: 65171
            m = p1.match(line)
            if m:
                group = m.groupdict()
                route_summary_information_dict = ret_dict.setdefault('route-summary-information', {})
                route_summary_information_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Router ID: 111.87.5.252
            m = p2.match(line)
            if m:
                group = m.groupdict()
                route_summary_information_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # inet.0: 929 destinations, 1615 routes (929 active, 0 holddown, 0 hidden)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                route_table = route_summary_information_dict. \
                    setdefault('route-table', [])
                route_table_dict = {k.replace('_', '-'):v for k, v in group.items() if v is not None}
                route_table.append(route_table_dict)
                continue
            
            #  Direct:      6 routes,      6 active
            m = p4.match(line)
            if m:
                group = m.groupdict()
                protocols_list = route_table_dict.setdefault('protocols', [])
                protocols_list.append({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

        return ret_dict