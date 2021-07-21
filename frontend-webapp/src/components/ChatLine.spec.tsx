import { render, screen } from '@testing-library/react'
import React from 'react'
import ChatLine from './ChatLine'
import ChatLineText from './ChatLineText'
import ChatLineCorrection from './ChatLineCorrection'

jest.mock('./ChatLineText')
jest.mock('./ChatLineCorrection')

describe('ChatLine', () => {
  const language = 'en-GB'
  const user = 'mock user'
  const text = 'mock text'
  const textLine = {
    language,
    user,
    text,
  }
  const correctionLine = {
    ...textLine,
    corrections: ['mock correction'],
  }

  beforeEach(jest.resetAllMocks)

  it('Renders a text line for a line without corrections', () => {
    render(<ChatLine line={textLine} />)
    expect(ChatLineText).toHaveBeenCalledTimes(1)
    expect(ChatLineText).toHaveBeenCalledWith(textLine)
    expect(ChatLineCorrection).not.toHaveBeenCalled()
  })
  it('Renders a correction line for a line with corrections', () => {
    render(<ChatLine line={correctionLine} />)
    expect(ChatLineCorrection).toHaveBeenCalledTimes(1)
    expect(ChatLineCorrection).toHaveBeenCalledWith(correctionLine)
    expect(ChatLineText).not.toHaveBeenCalled()
  })
})
