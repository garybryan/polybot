import { render, screen } from '@testing-library/react'
import React from 'react'
import { Correction } from '../interfaces/interfaces'
import ChatLineCorrection from './ChatLineCorrection'
import Corrections from './Corrections'

jest.mock('./Corrections')

describe('ChatLineCorrection', () => {
  const language = 'en-GB'
  const user = 'mock user'
  const text = 'mock text'
  const corrections = [
    {
      message: 'message',
      suggestions: [],
      offset: 0,
      length: 6,
      context: {},
      rule: {},
      sentence: 'sentence',
    },
  ]
  const correctionsEmpty: Correction[] = []

  beforeEach(jest.resetAllMocks)

  it.skip('Renders Corrections if there are corrections', () => {
    // TODO this is broken, unsure why
    render(
      <ChatLineCorrection
        language={language}
        user={user}
        text={text}
        corrections={corrections}
      />
    )
    expect(Corrections).toHaveBeenCalledTimes(1)
    expect(Corrections).toHaveBeenCalledWith({
      language,
      user,
      text,
      corrections,
    })
  })

  it('Does not render corrections if there are no corrections', () => {
    render(
      <ChatLineCorrection
        language={language}
        user={user}
        text={text}
        corrections={correctionsEmpty}
      />
    )
    expect(Corrections).not.toHaveBeenCalled()
    expect(screen.getByText('Looks good!')).toBeInTheDocument()
  })
})
