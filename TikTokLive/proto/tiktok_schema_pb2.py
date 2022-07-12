# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tiktok_schema.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13tiktok_schema.proto\x12\x06TikTok\"\x80\x02\n\x0fWebcastResponse\x12!\n\x08messages\x18\x01 \x03(\x0b\x32\x0f.TikTok.Message\x12\x0e\n\x06\x63ursor\x18\x02 \x01(\t\x12\x15\n\rfetchInterval\x18\x03 \x01(\x05\x12\x17\n\x0fserverTimestamp\x18\x04 \x01(\x03\x12\x13\n\x0binternalExt\x18\x05 \x01(\t\x12\x11\n\tfetchType\x18\x06 \x01(\x05\x12\'\n\x07wsParam\x18\x07 \x01(\x0b\x32\x16.TikTok.WebsocketParam\x12\x19\n\x11heartbeatDuration\x18\x08 \x01(\x05\x12\x0f\n\x07needAck\x18\t \x01(\x08\x12\r\n\x05wsUrl\x18\n \x01(\t\"\'\n\x07Message\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06\x62inary\x18\x02 \x01(\x0c\"-\n\x0eWebsocketParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\'\n\x15WebcastControlMessage\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\x05\"0\n\x19WebcastRoomUserSeqMessage\x12\x13\n\x0bviewerCount\x18\x03 \x01(\x05\"A\n\x12WebcastChatMessage\x12\x1a\n\x04user\x18\x02 \x01(\x0b\x32\x0c.TikTok.User\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\"p\n\x14WebcastMemberMessage\x12\x1a\n\x04user\x18\x02 \x01(\x0b\x32\x0c.TikTok.User\x12*\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x1b.TikTok.WebcastMessageEvent\x12\x10\n\x08\x61\x63tionId\x18\n \x01(\x05\"\xdc\x01\n\x12WebcastGiftMessage\x12\x1a\n\x04user\x18\x07 \x01(\x0b\x32\x0c.TikTok.User\x12\x0e\n\x06giftId\x18\x02 \x01(\x05\x12\x13\n\x0brepeatCount\x18\x05 \x01(\x05\x12\x11\n\trepeatEnd\x18\t \x01(\x05\x12:\n\x0bgiftDetails\x18\x0f \x01(\x0b\x32%.TikTok.WebcastGiftMessageGiftDetails\x12\x36\n\tgiftExtra\x18\x17 \x01(\x0b\x32#.TikTok.WebcastGiftMessageGiftExtra\"H\n\x1bWebcastGiftMessageGiftExtra\x12\x11\n\ttimestamp\x18\x06 \x01(\x04\x12\x16\n\x0ereceiverUserId\x18\x08 \x01(\x04\"\xa3\x01\n\x1dWebcastGiftMessageGiftDetails\x12\x36\n\tgiftImage\x18\x01 \x01(\x0b\x32#.TikTok.WebcastGiftMessageGiftImage\x12\x10\n\x08giftName\x18\x10 \x01(\t\x12\x10\n\x08\x64\x65scribe\x18\x02 \x01(\t\x12\x10\n\x08giftType\x18\x0b \x01(\x05\x12\x14\n\x0c\x64iamondCount\x18\x0c \x01(\x05\"5\n\x1bWebcastGiftMessageGiftImage\x12\x16\n\x0egiftPictureUrl\x18\x01 \x01(\t\"N\n\x14WebcastLinkMicBattle\x12\x36\n\x0b\x62\x61ttleUsers\x18\n \x03(\x0b\x32!.TikTok.WebcastLinkMicBattleItems\"S\n\x19WebcastLinkMicBattleItems\x12\x36\n\x0b\x62\x61ttleGroup\x18\x02 \x01(\x0b\x32!.TikTok.WebcastLinkMicBattleGroup\";\n\x19WebcastLinkMicBattleGroup\x12\x1e\n\x04user\x18\x01 \x01(\x0b\x32\x10.TikTok.LinkUser\"d\n\x14WebcastLinkMicArmies\x12\x36\n\x0b\x62\x61ttleItems\x18\x03 \x03(\x0b\x32!.TikTok.WebcastLinkMicArmiesItems\x12\x14\n\x0c\x62\x61ttleStatus\x18\x07 \x01(\x05\"h\n\x19WebcastLinkMicArmiesItems\x12\x12\n\nhostUserId\x18\x01 \x01(\x04\x12\x37\n\x0c\x62\x61ttleGroups\x18\x02 \x03(\x0b\x32!.TikTok.WebcastLinkMicArmiesGroup\"H\n\x19WebcastLinkMicArmiesGroup\x12\x1b\n\x05users\x18\x01 \x03(\x0b\x32\x0c.TikTok.User\x12\x0e\n\x06points\x18\x02 \x01(\x05\"^\n\x14WebcastSocialMessage\x12\x1a\n\x04user\x18\x02 \x01(\x0b\x32\x0c.TikTok.User\x12*\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x1b.TikTok.WebcastMessageEvent\"\x87\x01\n\x12WebcastLikeMessage\x12\x1a\n\x04user\x18\x05 \x01(\x0b\x32\x0c.TikTok.User\x12*\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x1b.TikTok.WebcastMessageEvent\x12\x11\n\tlikeCount\x18\x02 \x01(\x05\x12\x16\n\x0etotalLikeCount\x18\x03 \x01(\x05\"M\n\x19WebcastQuestionNewMessage\x12\x30\n\x0fquestionDetails\x18\x02 \x01(\x0b\x32\x17.TikTok.QuestionDetails\"C\n\x0fQuestionDetails\x12\x14\n\x0cquestionText\x18\x02 \x01(\t\x12\x1a\n\x04user\x18\x05 \x01(\x0b\x32\x0c.TikTok.User\"O\n\x13WebcastMessageEvent\x12\x38\n\x0c\x65ventDetails\x18\x08 \x01(\x0b\x32\".TikTok.WebcastMessageEventDetails\"@\n\x1aWebcastMessageEventDetails\x12\x13\n\x0b\x64isplayType\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\"\xce\x01\n\x04User\x12\x0e\n\x06userId\x18\x01 \x01(\x04\x12\x10\n\x08nickname\x18\x03 \x01(\t\x12.\n\x0eprofilePicture\x18\t \x01(\x0b\x32\x16.TikTok.ProfilePicture\x12\x34\n\x0f\x65xtraAttributes\x18\x16 \x01(\x0b\x32\x1b.TikTok.UserExtraAttributes\x12\x10\n\x08uniqueId\x18& \x01(\t\x12,\n\x06\x62\x61\x64ges\x18@ \x03(\x0b\x32\x1c.TikTok.UserBadgesAttributes\"n\n\x08LinkUser\x12\x0e\n\x06userId\x18\x01 \x01(\x04\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12.\n\x0eprofilePicture\x18\x03 \x01(\x0b\x32\x16.TikTok.ProfilePicture\x12\x10\n\x08uniqueId\x18\x04 \x01(\t\"\x1e\n\x0eProfilePicture\x12\x0c\n\x04urls\x18\x01 \x03(\t\")\n\x13UserExtraAttributes\x12\x12\n\nfollowRole\x18\x03 \x01(\x05\"f\n\x14UserBadgesAttributes\x12!\n\x06\x62\x61\x64ges\x18\x15 \x03(\x0b\x32\x11.TikTok.UserBadge\x12+\n\x0bimageBadges\x18\x14 \x03(\x0b\x32\x16.TikTok.UserImageBadge\"\'\n\tUserBadge\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"C\n\x17WebcastWebsocketMessage\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x0c\n\x04type\x18\x07 \x01(\t\x12\x0e\n\x06\x62inary\x18\x08 \x01(\x0c\"/\n\x13WebcastWebsocketAck\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x0c\n\x04type\x18\x07 \x01(\t\"V\n\x17WebcastLiveIntroMessage\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x1a\n\x04user\x18\x05 \x01(\x0b\x32\x0c.TikTok.User\"$\n\rSystemMessage\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"*\n\x1aWebcastInRoomBannerMessage\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"&\n\x08RankItem\x12\x0e\n\x06\x63olour\x18\x01 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\x04\"L\n\rWeeklyRanking\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x1e\n\x04rank\x18\x03 \x01(\x0b\x32\x10.TikTok.RankItem\"8\n\rRankContainer\x12\'\n\x08rankings\x18\x04 \x01(\x0b\x32\x15.TikTok.WeeklyRanking\"?\n\x18WebcastHourlyRankMessage\x12#\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x15.TikTok.RankContainer\"Q\n\x0eUserImageBadge\x12\x13\n\x0b\x64isplayType\x18\x01 \x01(\x05\x12*\n\x05image\x18\x02 \x01(\x0b\x32\x1b.TikTok.UserImageBadgeImage\"\"\n\x13UserImageBadgeImage\x12\x0b\n\x03url\x18\x01 \x01(\t\"Z\n\x17WebcastEmoteChatMessage\x12\x1a\n\x04user\x18\x02 \x01(\x0b\x32\x0c.TikTok.User\x12#\n\x05\x65mote\x18\x03 \x01(\x0b\x32\x14.TikTok.EmoteDetails\"B\n\x0c\x45moteDetails\x12\x0f\n\x07\x65moteId\x18\x01 \x01(\t\x12!\n\x05image\x18\x02 \x01(\x0b\x32\x12.TikTok.EmoteImage\"\x1e\n\nEmoteImage\x12\x10\n\x08imageUrl\x18\x01 \x01(\t\"|\n\x16WebcastEnvelopeMessage\x12\x30\n\x0ftreasureBoxData\x18\x02 \x01(\x0b\x32\x17.TikTok.TreasureBoxData\x12\x30\n\x0ftreasureBoxUser\x18\x01 \x01(\x0b\x32\x17.TikTok.TreasureBoxUser\":\n\x0fTreasureBoxUser\x12\'\n\x05user2\x18\x08 \x01(\x0b\x32\x18.TikTok.TreasureBoxUser2\";\n\x10TreasureBoxUser2\x12\'\n\x05user3\x18\x04 \x03(\x0b\x32\x18.TikTok.TreasureBoxUser3\";\n\x10TreasureBoxUser3\x12\'\n\x05user4\x18\x15 \x01(\x0b\x32\x18.TikTok.TreasureBoxUser4\".\n\x10TreasureBoxUser4\x12\x1a\n\x04user\x18\x01 \x01(\x0b\x32\x0c.TikTok.User\"D\n\x0fTreasureBoxData\x12\r\n\x05\x63oins\x18\x05 \x01(\r\x12\x0f\n\x07\x63\x61nOpen\x18\x06 \x01(\r\x12\x11\n\ttimestamp\x18\x07 \x01(\x04\x62\x06proto3')



_WEBCASTRESPONSE = DESCRIPTOR.message_types_by_name['WebcastResponse']
_MESSAGE = DESCRIPTOR.message_types_by_name['Message']
_WEBSOCKETPARAM = DESCRIPTOR.message_types_by_name['WebsocketParam']
_WEBCASTCONTROLMESSAGE = DESCRIPTOR.message_types_by_name['WebcastControlMessage']
_WEBCASTROOMUSERSEQMESSAGE = DESCRIPTOR.message_types_by_name['WebcastRoomUserSeqMessage']
_WEBCASTCHATMESSAGE = DESCRIPTOR.message_types_by_name['WebcastChatMessage']
_WEBCASTMEMBERMESSAGE = DESCRIPTOR.message_types_by_name['WebcastMemberMessage']
_WEBCASTGIFTMESSAGE = DESCRIPTOR.message_types_by_name['WebcastGiftMessage']
_WEBCASTGIFTMESSAGEGIFTEXTRA = DESCRIPTOR.message_types_by_name['WebcastGiftMessageGiftExtra']
_WEBCASTGIFTMESSAGEGIFTDETAILS = DESCRIPTOR.message_types_by_name['WebcastGiftMessageGiftDetails']
_WEBCASTGIFTMESSAGEGIFTIMAGE = DESCRIPTOR.message_types_by_name['WebcastGiftMessageGiftImage']
_WEBCASTLINKMICBATTLE = DESCRIPTOR.message_types_by_name['WebcastLinkMicBattle']
_WEBCASTLINKMICBATTLEITEMS = DESCRIPTOR.message_types_by_name['WebcastLinkMicBattleItems']
_WEBCASTLINKMICBATTLEGROUP = DESCRIPTOR.message_types_by_name['WebcastLinkMicBattleGroup']
_WEBCASTLINKMICARMIES = DESCRIPTOR.message_types_by_name['WebcastLinkMicArmies']
_WEBCASTLINKMICARMIESITEMS = DESCRIPTOR.message_types_by_name['WebcastLinkMicArmiesItems']
_WEBCASTLINKMICARMIESGROUP = DESCRIPTOR.message_types_by_name['WebcastLinkMicArmiesGroup']
_WEBCASTSOCIALMESSAGE = DESCRIPTOR.message_types_by_name['WebcastSocialMessage']
_WEBCASTLIKEMESSAGE = DESCRIPTOR.message_types_by_name['WebcastLikeMessage']
_WEBCASTQUESTIONNEWMESSAGE = DESCRIPTOR.message_types_by_name['WebcastQuestionNewMessage']
_QUESTIONDETAILS = DESCRIPTOR.message_types_by_name['QuestionDetails']
_WEBCASTMESSAGEEVENT = DESCRIPTOR.message_types_by_name['WebcastMessageEvent']
_WEBCASTMESSAGEEVENTDETAILS = DESCRIPTOR.message_types_by_name['WebcastMessageEventDetails']
_USER = DESCRIPTOR.message_types_by_name['User']
_LINKUSER = DESCRIPTOR.message_types_by_name['LinkUser']
_PROFILEPICTURE = DESCRIPTOR.message_types_by_name['ProfilePicture']
_USEREXTRAATTRIBUTES = DESCRIPTOR.message_types_by_name['UserExtraAttributes']
_USERBADGESATTRIBUTES = DESCRIPTOR.message_types_by_name['UserBadgesAttributes']
_USERBADGE = DESCRIPTOR.message_types_by_name['UserBadge']
_WEBCASTWEBSOCKETMESSAGE = DESCRIPTOR.message_types_by_name['WebcastWebsocketMessage']
_WEBCASTWEBSOCKETACK = DESCRIPTOR.message_types_by_name['WebcastWebsocketAck']
_WEBCASTLIVEINTROMESSAGE = DESCRIPTOR.message_types_by_name['WebcastLiveIntroMessage']
_SYSTEMMESSAGE = DESCRIPTOR.message_types_by_name['SystemMessage']
_WEBCASTINROOMBANNERMESSAGE = DESCRIPTOR.message_types_by_name['WebcastInRoomBannerMessage']
_RANKITEM = DESCRIPTOR.message_types_by_name['RankItem']
_WEEKLYRANKING = DESCRIPTOR.message_types_by_name['WeeklyRanking']
_RANKCONTAINER = DESCRIPTOR.message_types_by_name['RankContainer']
_WEBCASTHOURLYRANKMESSAGE = DESCRIPTOR.message_types_by_name['WebcastHourlyRankMessage']
_USERIMAGEBADGE = DESCRIPTOR.message_types_by_name['UserImageBadge']
_USERIMAGEBADGEIMAGE = DESCRIPTOR.message_types_by_name['UserImageBadgeImage']
_WEBCASTEMOTECHATMESSAGE = DESCRIPTOR.message_types_by_name['WebcastEmoteChatMessage']
_EMOTEDETAILS = DESCRIPTOR.message_types_by_name['EmoteDetails']
_EMOTEIMAGE = DESCRIPTOR.message_types_by_name['EmoteImage']
_WEBCASTENVELOPEMESSAGE = DESCRIPTOR.message_types_by_name['WebcastEnvelopeMessage']
_TREASUREBOXUSER = DESCRIPTOR.message_types_by_name['TreasureBoxUser']
_TREASUREBOXUSER2 = DESCRIPTOR.message_types_by_name['TreasureBoxUser2']
_TREASUREBOXUSER3 = DESCRIPTOR.message_types_by_name['TreasureBoxUser3']
_TREASUREBOXUSER4 = DESCRIPTOR.message_types_by_name['TreasureBoxUser4']
_TREASUREBOXDATA = DESCRIPTOR.message_types_by_name['TreasureBoxData']
WebcastResponse = _reflection.GeneratedProtocolMessageType('WebcastResponse', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTRESPONSE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastResponse)
  })
_sym_db.RegisterMessage(WebcastResponse)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.Message)
  })
_sym_db.RegisterMessage(Message)

WebsocketParam = _reflection.GeneratedProtocolMessageType('WebsocketParam', (_message.Message,), {
  'DESCRIPTOR' : _WEBSOCKETPARAM,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebsocketParam)
  })
_sym_db.RegisterMessage(WebsocketParam)

WebcastControlMessage = _reflection.GeneratedProtocolMessageType('WebcastControlMessage', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTCONTROLMESSAGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastControlMessage)
  })
_sym_db.RegisterMessage(WebcastControlMessage)

WebcastRoomUserSeqMessage = _reflection.GeneratedProtocolMessageType('WebcastRoomUserSeqMessage', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTROOMUSERSEQMESSAGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastRoomUserSeqMessage)
  })
_sym_db.RegisterMessage(WebcastRoomUserSeqMessage)

WebcastChatMessage = _reflection.GeneratedProtocolMessageType('WebcastChatMessage', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTCHATMESSAGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastChatMessage)
  })
_sym_db.RegisterMessage(WebcastChatMessage)

WebcastMemberMessage = _reflection.GeneratedProtocolMessageType('WebcastMemberMessage', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTMEMBERMESSAGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastMemberMessage)
  })
_sym_db.RegisterMessage(WebcastMemberMessage)

WebcastGiftMessage = _reflection.GeneratedProtocolMessageType('WebcastGiftMessage', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTGIFTMESSAGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastGiftMessage)
  })
_sym_db.RegisterMessage(WebcastGiftMessage)

WebcastGiftMessageGiftExtra = _reflection.GeneratedProtocolMessageType('WebcastGiftMessageGiftExtra', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTGIFTMESSAGEGIFTEXTRA,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastGiftMessageGiftExtra)
  })
_sym_db.RegisterMessage(WebcastGiftMessageGiftExtra)

WebcastGiftMessageGiftDetails = _reflection.GeneratedProtocolMessageType('WebcastGiftMessageGiftDetails', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTGIFTMESSAGEGIFTDETAILS,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastGiftMessageGiftDetails)
  })
_sym_db.RegisterMessage(WebcastGiftMessageGiftDetails)

WebcastGiftMessageGiftImage = _reflection.GeneratedProtocolMessageType('WebcastGiftMessageGiftImage', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTGIFTMESSAGEGIFTIMAGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastGiftMessageGiftImage)
  })
_sym_db.RegisterMessage(WebcastGiftMessageGiftImage)

WebcastLinkMicBattle = _reflection.GeneratedProtocolMessageType('WebcastLinkMicBattle', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTLINKMICBATTLE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastLinkMicBattle)
  })
_sym_db.RegisterMessage(WebcastLinkMicBattle)

WebcastLinkMicBattleItems = _reflection.GeneratedProtocolMessageType('WebcastLinkMicBattleItems', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTLINKMICBATTLEITEMS,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastLinkMicBattleItems)
  })
_sym_db.RegisterMessage(WebcastLinkMicBattleItems)

WebcastLinkMicBattleGroup = _reflection.GeneratedProtocolMessageType('WebcastLinkMicBattleGroup', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTLINKMICBATTLEGROUP,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastLinkMicBattleGroup)
  })
_sym_db.RegisterMessage(WebcastLinkMicBattleGroup)

WebcastLinkMicArmies = _reflection.GeneratedProtocolMessageType('WebcastLinkMicArmies', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTLINKMICARMIES,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastLinkMicArmies)
  })
_sym_db.RegisterMessage(WebcastLinkMicArmies)

WebcastLinkMicArmiesItems = _reflection.GeneratedProtocolMessageType('WebcastLinkMicArmiesItems', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTLINKMICARMIESITEMS,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastLinkMicArmiesItems)
  })
_sym_db.RegisterMessage(WebcastLinkMicArmiesItems)

WebcastLinkMicArmiesGroup = _reflection.GeneratedProtocolMessageType('WebcastLinkMicArmiesGroup', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTLINKMICARMIESGROUP,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastLinkMicArmiesGroup)
  })
_sym_db.RegisterMessage(WebcastLinkMicArmiesGroup)

WebcastSocialMessage = _reflection.GeneratedProtocolMessageType('WebcastSocialMessage', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTSOCIALMESSAGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastSocialMessage)
  })
_sym_db.RegisterMessage(WebcastSocialMessage)

WebcastLikeMessage = _reflection.GeneratedProtocolMessageType('WebcastLikeMessage', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTLIKEMESSAGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastLikeMessage)
  })
_sym_db.RegisterMessage(WebcastLikeMessage)

WebcastQuestionNewMessage = _reflection.GeneratedProtocolMessageType('WebcastQuestionNewMessage', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTQUESTIONNEWMESSAGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastQuestionNewMessage)
  })
_sym_db.RegisterMessage(WebcastQuestionNewMessage)

QuestionDetails = _reflection.GeneratedProtocolMessageType('QuestionDetails', (_message.Message,), {
  'DESCRIPTOR' : _QUESTIONDETAILS,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.QuestionDetails)
  })
_sym_db.RegisterMessage(QuestionDetails)

WebcastMessageEvent = _reflection.GeneratedProtocolMessageType('WebcastMessageEvent', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTMESSAGEEVENT,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastMessageEvent)
  })
_sym_db.RegisterMessage(WebcastMessageEvent)

WebcastMessageEventDetails = _reflection.GeneratedProtocolMessageType('WebcastMessageEventDetails', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTMESSAGEEVENTDETAILS,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastMessageEventDetails)
  })
_sym_db.RegisterMessage(WebcastMessageEventDetails)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.User)
  })
_sym_db.RegisterMessage(User)

LinkUser = _reflection.GeneratedProtocolMessageType('LinkUser', (_message.Message,), {
  'DESCRIPTOR' : _LINKUSER,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.LinkUser)
  })
_sym_db.RegisterMessage(LinkUser)

ProfilePicture = _reflection.GeneratedProtocolMessageType('ProfilePicture', (_message.Message,), {
  'DESCRIPTOR' : _PROFILEPICTURE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.ProfilePicture)
  })
_sym_db.RegisterMessage(ProfilePicture)

UserExtraAttributes = _reflection.GeneratedProtocolMessageType('UserExtraAttributes', (_message.Message,), {
  'DESCRIPTOR' : _USEREXTRAATTRIBUTES,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.UserExtraAttributes)
  })
_sym_db.RegisterMessage(UserExtraAttributes)

UserBadgesAttributes = _reflection.GeneratedProtocolMessageType('UserBadgesAttributes', (_message.Message,), {
  'DESCRIPTOR' : _USERBADGESATTRIBUTES,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.UserBadgesAttributes)
  })
_sym_db.RegisterMessage(UserBadgesAttributes)

UserBadge = _reflection.GeneratedProtocolMessageType('UserBadge', (_message.Message,), {
  'DESCRIPTOR' : _USERBADGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.UserBadge)
  })
_sym_db.RegisterMessage(UserBadge)

WebcastWebsocketMessage = _reflection.GeneratedProtocolMessageType('WebcastWebsocketMessage', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTWEBSOCKETMESSAGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastWebsocketMessage)
  })
_sym_db.RegisterMessage(WebcastWebsocketMessage)

WebcastWebsocketAck = _reflection.GeneratedProtocolMessageType('WebcastWebsocketAck', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTWEBSOCKETACK,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastWebsocketAck)
  })
_sym_db.RegisterMessage(WebcastWebsocketAck)

WebcastLiveIntroMessage = _reflection.GeneratedProtocolMessageType('WebcastLiveIntroMessage', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTLIVEINTROMESSAGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastLiveIntroMessage)
  })
_sym_db.RegisterMessage(WebcastLiveIntroMessage)

SystemMessage = _reflection.GeneratedProtocolMessageType('SystemMessage', (_message.Message,), {
  'DESCRIPTOR' : _SYSTEMMESSAGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.SystemMessage)
  })
_sym_db.RegisterMessage(SystemMessage)

WebcastInRoomBannerMessage = _reflection.GeneratedProtocolMessageType('WebcastInRoomBannerMessage', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTINROOMBANNERMESSAGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastInRoomBannerMessage)
  })
_sym_db.RegisterMessage(WebcastInRoomBannerMessage)

RankItem = _reflection.GeneratedProtocolMessageType('RankItem', (_message.Message,), {
  'DESCRIPTOR' : _RANKITEM,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.RankItem)
  })
_sym_db.RegisterMessage(RankItem)

WeeklyRanking = _reflection.GeneratedProtocolMessageType('WeeklyRanking', (_message.Message,), {
  'DESCRIPTOR' : _WEEKLYRANKING,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WeeklyRanking)
  })
_sym_db.RegisterMessage(WeeklyRanking)

RankContainer = _reflection.GeneratedProtocolMessageType('RankContainer', (_message.Message,), {
  'DESCRIPTOR' : _RANKCONTAINER,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.RankContainer)
  })
_sym_db.RegisterMessage(RankContainer)

WebcastHourlyRankMessage = _reflection.GeneratedProtocolMessageType('WebcastHourlyRankMessage', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTHOURLYRANKMESSAGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastHourlyRankMessage)
  })
_sym_db.RegisterMessage(WebcastHourlyRankMessage)

UserImageBadge = _reflection.GeneratedProtocolMessageType('UserImageBadge', (_message.Message,), {
  'DESCRIPTOR' : _USERIMAGEBADGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.UserImageBadge)
  })
_sym_db.RegisterMessage(UserImageBadge)

UserImageBadgeImage = _reflection.GeneratedProtocolMessageType('UserImageBadgeImage', (_message.Message,), {
  'DESCRIPTOR' : _USERIMAGEBADGEIMAGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.UserImageBadgeImage)
  })
_sym_db.RegisterMessage(UserImageBadgeImage)

WebcastEmoteChatMessage = _reflection.GeneratedProtocolMessageType('WebcastEmoteChatMessage', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTEMOTECHATMESSAGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastEmoteChatMessage)
  })
_sym_db.RegisterMessage(WebcastEmoteChatMessage)

EmoteDetails = _reflection.GeneratedProtocolMessageType('EmoteDetails', (_message.Message,), {
  'DESCRIPTOR' : _EMOTEDETAILS,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.EmoteDetails)
  })
_sym_db.RegisterMessage(EmoteDetails)

EmoteImage = _reflection.GeneratedProtocolMessageType('EmoteImage', (_message.Message,), {
  'DESCRIPTOR' : _EMOTEIMAGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.EmoteImage)
  })
_sym_db.RegisterMessage(EmoteImage)

WebcastEnvelopeMessage = _reflection.GeneratedProtocolMessageType('WebcastEnvelopeMessage', (_message.Message,), {
  'DESCRIPTOR' : _WEBCASTENVELOPEMESSAGE,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.WebcastEnvelopeMessage)
  })
_sym_db.RegisterMessage(WebcastEnvelopeMessage)

TreasureBoxUser = _reflection.GeneratedProtocolMessageType('TreasureBoxUser', (_message.Message,), {
  'DESCRIPTOR' : _TREASUREBOXUSER,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.TreasureBoxUser)
  })
_sym_db.RegisterMessage(TreasureBoxUser)

TreasureBoxUser2 = _reflection.GeneratedProtocolMessageType('TreasureBoxUser2', (_message.Message,), {
  'DESCRIPTOR' : _TREASUREBOXUSER2,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.TreasureBoxUser2)
  })
_sym_db.RegisterMessage(TreasureBoxUser2)

TreasureBoxUser3 = _reflection.GeneratedProtocolMessageType('TreasureBoxUser3', (_message.Message,), {
  'DESCRIPTOR' : _TREASUREBOXUSER3,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.TreasureBoxUser3)
  })
_sym_db.RegisterMessage(TreasureBoxUser3)

TreasureBoxUser4 = _reflection.GeneratedProtocolMessageType('TreasureBoxUser4', (_message.Message,), {
  'DESCRIPTOR' : _TREASUREBOXUSER4,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.TreasureBoxUser4)
  })
_sym_db.RegisterMessage(TreasureBoxUser4)

TreasureBoxData = _reflection.GeneratedProtocolMessageType('TreasureBoxData', (_message.Message,), {
  'DESCRIPTOR' : _TREASUREBOXDATA,
  '__module__' : 'tiktok_schema_pb2'
  # @@protoc_insertion_point(class_scope:TikTok.TreasureBoxData)
  })
_sym_db.RegisterMessage(TreasureBoxData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WEBCASTRESPONSE._serialized_start=32
  _WEBCASTRESPONSE._serialized_end=288
  _MESSAGE._serialized_start=290
  _MESSAGE._serialized_end=329
  _WEBSOCKETPARAM._serialized_start=331
  _WEBSOCKETPARAM._serialized_end=376
  _WEBCASTCONTROLMESSAGE._serialized_start=378
  _WEBCASTCONTROLMESSAGE._serialized_end=417
  _WEBCASTROOMUSERSEQMESSAGE._serialized_start=419
  _WEBCASTROOMUSERSEQMESSAGE._serialized_end=467
  _WEBCASTCHATMESSAGE._serialized_start=469
  _WEBCASTCHATMESSAGE._serialized_end=534
  _WEBCASTMEMBERMESSAGE._serialized_start=536
  _WEBCASTMEMBERMESSAGE._serialized_end=648
  _WEBCASTGIFTMESSAGE._serialized_start=651
  _WEBCASTGIFTMESSAGE._serialized_end=871
  _WEBCASTGIFTMESSAGEGIFTEXTRA._serialized_start=873
  _WEBCASTGIFTMESSAGEGIFTEXTRA._serialized_end=945
  _WEBCASTGIFTMESSAGEGIFTDETAILS._serialized_start=948
  _WEBCASTGIFTMESSAGEGIFTDETAILS._serialized_end=1111
  _WEBCASTGIFTMESSAGEGIFTIMAGE._serialized_start=1113
  _WEBCASTGIFTMESSAGEGIFTIMAGE._serialized_end=1166
  _WEBCASTLINKMICBATTLE._serialized_start=1168
  _WEBCASTLINKMICBATTLE._serialized_end=1246
  _WEBCASTLINKMICBATTLEITEMS._serialized_start=1248
  _WEBCASTLINKMICBATTLEITEMS._serialized_end=1331
  _WEBCASTLINKMICBATTLEGROUP._serialized_start=1333
  _WEBCASTLINKMICBATTLEGROUP._serialized_end=1392
  _WEBCASTLINKMICARMIES._serialized_start=1394
  _WEBCASTLINKMICARMIES._serialized_end=1494
  _WEBCASTLINKMICARMIESITEMS._serialized_start=1496
  _WEBCASTLINKMICARMIESITEMS._serialized_end=1600
  _WEBCASTLINKMICARMIESGROUP._serialized_start=1602
  _WEBCASTLINKMICARMIESGROUP._serialized_end=1674
  _WEBCASTSOCIALMESSAGE._serialized_start=1676
  _WEBCASTSOCIALMESSAGE._serialized_end=1770
  _WEBCASTLIKEMESSAGE._serialized_start=1773
  _WEBCASTLIKEMESSAGE._serialized_end=1908
  _WEBCASTQUESTIONNEWMESSAGE._serialized_start=1910
  _WEBCASTQUESTIONNEWMESSAGE._serialized_end=1987
  _QUESTIONDETAILS._serialized_start=1989
  _QUESTIONDETAILS._serialized_end=2056
  _WEBCASTMESSAGEEVENT._serialized_start=2058
  _WEBCASTMESSAGEEVENT._serialized_end=2137
  _WEBCASTMESSAGEEVENTDETAILS._serialized_start=2139
  _WEBCASTMESSAGEEVENTDETAILS._serialized_end=2203
  _USER._serialized_start=2206
  _USER._serialized_end=2412
  _LINKUSER._serialized_start=2414
  _LINKUSER._serialized_end=2524
  _PROFILEPICTURE._serialized_start=2526
  _PROFILEPICTURE._serialized_end=2556
  _USEREXTRAATTRIBUTES._serialized_start=2558
  _USEREXTRAATTRIBUTES._serialized_end=2599
  _USERBADGESATTRIBUTES._serialized_start=2601
  _USERBADGESATTRIBUTES._serialized_end=2703
  _USERBADGE._serialized_start=2705
  _USERBADGE._serialized_end=2744
  _WEBCASTWEBSOCKETMESSAGE._serialized_start=2746
  _WEBCASTWEBSOCKETMESSAGE._serialized_end=2813
  _WEBCASTWEBSOCKETACK._serialized_start=2815
  _WEBCASTWEBSOCKETACK._serialized_end=2862
  _WEBCASTLIVEINTROMESSAGE._serialized_start=2864
  _WEBCASTLIVEINTROMESSAGE._serialized_end=2950
  _SYSTEMMESSAGE._serialized_start=2952
  _SYSTEMMESSAGE._serialized_end=2988
  _WEBCASTINROOMBANNERMESSAGE._serialized_start=2990
  _WEBCASTINROOMBANNERMESSAGE._serialized_end=3032
  _RANKITEM._serialized_start=3034
  _RANKITEM._serialized_end=3072
  _WEEKLYRANKING._serialized_start=3074
  _WEEKLYRANKING._serialized_end=3150
  _RANKCONTAINER._serialized_start=3152
  _RANKCONTAINER._serialized_end=3208
  _WEBCASTHOURLYRANKMESSAGE._serialized_start=3210
  _WEBCASTHOURLYRANKMESSAGE._serialized_end=3273
  _USERIMAGEBADGE._serialized_start=3275
  _USERIMAGEBADGE._serialized_end=3356
  _USERIMAGEBADGEIMAGE._serialized_start=3358
  _USERIMAGEBADGEIMAGE._serialized_end=3392
  _WEBCASTEMOTECHATMESSAGE._serialized_start=3394
  _WEBCASTEMOTECHATMESSAGE._serialized_end=3484
  _EMOTEDETAILS._serialized_start=3486
  _EMOTEDETAILS._serialized_end=3552
  _EMOTEIMAGE._serialized_start=3554
  _EMOTEIMAGE._serialized_end=3584
  _WEBCASTENVELOPEMESSAGE._serialized_start=3586
  _WEBCASTENVELOPEMESSAGE._serialized_end=3710
  _TREASUREBOXUSER._serialized_start=3712
  _TREASUREBOXUSER._serialized_end=3770
  _TREASUREBOXUSER2._serialized_start=3772
  _TREASUREBOXUSER2._serialized_end=3831
  _TREASUREBOXUSER3._serialized_start=3833
  _TREASUREBOXUSER3._serialized_end=3892
  _TREASUREBOXUSER4._serialized_start=3894
  _TREASUREBOXUSER4._serialized_end=3940
  _TREASUREBOXDATA._serialized_start=3942
  _TREASUREBOXDATA._serialized_end=4010
# @@protoc_insertion_point(module_scope)
