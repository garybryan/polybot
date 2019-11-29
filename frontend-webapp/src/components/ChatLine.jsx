import React from 'react'
import PropTypes from 'prop-types'

export default function ChatLine ({ user, text }) {
  return (
    <div className="ChatLine"><strong>{ user }:</strong> { text }</div>
  )
}

ChatLine.propTypes = {
  user: PropTypes.string,
  text: PropTypes.string
}
