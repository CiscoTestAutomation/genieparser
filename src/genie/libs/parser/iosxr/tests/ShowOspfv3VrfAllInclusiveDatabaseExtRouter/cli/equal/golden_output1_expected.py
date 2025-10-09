expected_output = {
		'vrf': {
			'default': {
				'address_family': {
					'ipv6': {
						'instance': {
							'1': {
								'areas': {
									0: {
										'database': {
											'lsa_types': {
												33: {
													'lsa_type': 33,
													'lsas': {
														'0 1.1.1.1': {
															'adv_router': '1.1.1.1',
															'lsa_id': 0,
															'ospfv3': {
																'header': {
																	'age': 69,
																	'type': 'Extended Router Links',
																	'lsa_id': 0,
																	'adv_router': '1.1.1.1',
																	'seq_num': '80000001',
																	'checksum': '0xb361',
																	'length': 72,
																	},
																'body': {
																	'num_of_tlvs': 1,
																	'tlvs': {
																		1: {
																			'type': 1,
																			'type_desc': 'Router Link',
																			'value': {
                                                                                'tlv_value': {
																					'link': {
																						'link_info': {
																							'link_type': 'another router (point-to-point)',
																							'link_metric': 1,
																							'local_interface_id': 109,
																							'neighbor_interface_id': 16,
																							'neighbor_router_id': '1.1.1.2',
																							},
																						},
																					'num_of_subtlvs': 1,
																					'subtlv': {
																						1: {
																							'value': {
																								'subtlv_value': {
																									'optical_info': {
																										'optical_info': {
																											'enterprise_num': 9,
																											'opaque_value': '76312e30302d4f4c542d435f305f305f30202020',
																											},
																										},
																									},
																								},
																							'subtype': 32770,
																							'subtype_desc': 'Optical Link Info',
																							'length': 24,
																							},
																						},
																					},
																				},
																			'length': 44,
																			},
																		},
																	},
																},
															},
															'0 1.1.1.2': {
																	'adv_router': '1.1.1.2',
																	'lsa_id': 0,
																	'ospfv3': {
																		'header': {
																			'age': 39,
																			'type': 'Extended Router Links',
																			'lsa_id': 0,
																			'adv_router': '1.1.1.2',
																			'seq_num': '80000002',
																			'checksum': '0xc3d',
																			'length': 120,
																			},
																		'body': {
																			'num_of_tlvs': 2,
																			'tlvs': {
																				1: {
																					'type': 1,
																					'type_desc': 'Router Link',
																					'value': {
																						'tlv_value': {
																							'link': {
																								'link_info': {
																									'link_type': 'another router (point-to-point)',
																									'link_metric': 1,
																									'local_interface_id': 16,
																									'neighbor_interface_id': 109,
																									'neighbor_router_id': '1.1.1.1',
																									},
																								},
																							'num_of_subtlvs': 1,
																							'subtlv': {
																								1: {
																									'value': {
																										'subtlv_value': {
																											'optical_info': {
																												'optical_info': {
																													'enterprise_num': 9,
																													'opaque_value': '76312e30302d494c412d435f305f305f32202020',
																													},
																												},
																											},
																										},
																									'subtype': 32770,
																									'subtype_desc': 'Optical Link Info',
																									'length': 24,
																									},
																								},
																							},
																						},
																					'length': 44,
																					},
																				2: {
																					'type': 1,
																					'type_desc': 'Router Link',
																					'value': {
																						'tlv_value': {
																							'link': {
																								'link_info': {
																									'link_type': 'another router (point-to-point)',
																									'link_metric': 1,
																									'local_interface_id': 15,
																									'neighbor_interface_id': 16,
																									'neighbor_router_id': '1.1.1.3',
																									},
																								},
																							'num_of_subtlvs': 1,
																							'subtlv': {
																								1: {
																									'value': {
																										'subtlv_value': {
																											'optical_info': {
																												'optical_info': {
																													'enterprise_num': 9,
																													'opaque_value': '76312e30302d494c412d435f305f305f30202020',
																													},
																												},
																											},
																										},
																									'subtype': 32770,
																									'subtype_desc': 'Optical Link Info',
																									'length': 24,
																									},
																								},
																							},
																						},
																					'length': 44,
																					},
																  },
																},
															  },
															},
															'0 1.1.1.3': {
																	'adv_router': '1.1.1.3',
																	'lsa_id': 0,
																	'ospfv3': {
																		'header': {
																			'age': 15,
																			'type': 'Extended Router Links',
																			'lsa_id': 0,
																			'adv_router': '1.1.1.3',
																			'seq_num': '80000002',
																			'checksum': '0xfd8a',
																			'length': 120,
																			},
																		'body': {
																			'num_of_tlvs': 2,
																			'tlvs': {
																				1: {
																					'type': 1,
																					'type_desc': 'Router Link',
																					'value': {
																						'tlv_value': {
																							'link': {
																								'link_info': {
																									'link_type': 'another router (point-to-point)',
																									'link_metric': 1,
																									'local_interface_id': 16,
																									'neighbor_interface_id': 15,
																									'neighbor_router_id': '1.1.1.2',
																									},
																								},
																							'num_of_subtlvs': 1,
																							'subtlv': {
																								1: {
																									'value': {
																										'subtlv_value': {
																											'optical_info': {
																												'optical_info': {
																													'enterprise_num': 9,
																													'opaque_value': '76312e30302d494c412d435f305f305f32202020',
																													},
																												},
																											},
																										},
																									'subtype': 32770,
																									'subtype_desc': 'Optical Link Info',
																									'length': 24,
																									},
																								},
																							},
																						},
																					'length': 44,
																					},
																				2: {
																					'type': 1,
																					'type_desc': 'Router Link',
																					'value': {
																						'tlv_value': {
																							'link': {
																								'link_info': {
																									'link_type': 'another router (point-to-point)',
																									'link_metric': 1,
																									'local_interface_id': 15,
																									'neighbor_interface_id': 44,
																									'neighbor_router_id': '1.1.1.4',
																									},
																								},
																							'num_of_subtlvs': 1,
																							'subtlv': {
																								1: {
																									'value': {
																										'subtlv_value': {
																											'optical_info': {
																												'optical_info': {
																													'enterprise_num': 9,
																													'opaque_value': '76312e30302d494c412d435f305f305f30202020',
																													},
																												},
																											},
																										},
																									'subtype': 32770,
																									'subtype_desc': 'Optical Link Info',
																									'length': 24,
																									},
																								},
																							},
																						},
																					'length': 44,
																					},
																  },
																},
															  },
															},
															'0 1.1.1.4': {
																	'adv_router': '1.1.1.4',
																	'lsa_id': 0,
																	'ospfv3': {
																		'header': {
																			'age': 16,
																			'type': 'Extended Router Links',
																			'lsa_id': 0,
																			'adv_router': '1.1.1.4',
																			'seq_num': '80000001',
																			'checksum': '0xf44',
																			'length': 72,
																			},
																		'body': {
																			'num_of_tlvs': 1,
																			'tlvs': {
																				1: {
																					'type': 1,
																					'type_desc': 'Router Link',
																					'value': {
																						'tlv_value': {
																							'link': {
																								'link_info': {
																									'link_type': 'another router (point-to-point)',
																									'link_metric': 1,
																									'local_interface_id': 44,
																									'neighbor_interface_id': 15,
																									'neighbor_router_id': '1.1.1.3',
																									},
																								},
																							'num_of_subtlvs': 1,
																							'subtlv': {
																								1: {
																									'value': {
																										'subtlv_value': {
																											'optical_info': {
																												'optical_info': {
																													'enterprise_num': 9,
																													'opaque_value': '76312e30302d4f4c542d435f305f305f30202020',
																													},
																												},
																											},
																										},
																									'subtype': 32770,
																									'subtype_desc': 'Optical Link Info',
																									'length': 24,
																									},
																								},
																							},
																						},
																					'length': 44,
																					},
																				},
																			},
															  },
															},
														  },
														},
													  },
													},
												  },
												},
											  },
											},
										  },
										},
									  },
									},
								  }
