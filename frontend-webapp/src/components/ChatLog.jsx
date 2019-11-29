import React from 'react'
import ScrollableFeed from 'react-scrollable-feed'
import PropTypes from 'prop-types'

import ChatLine from './ChatLine'

export default function ChatLog ({ log }) {
  return (
    <ScrollableFeed className="ChatLogContainer" viewableDetectionEpsilon={15}>
      {
        log.map((line, index) =>
          <ChatLine { ...line } key={index} />
        )
      }
    </ScrollableFeed>
  )
}

ChatLog.propTypes = {
  log: PropTypes.array
}
