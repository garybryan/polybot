import React from 'react'
import { render, screen } from '@testing-library/react'
import ChatLog from './ChatLog'

describe('ChatLog', () => {
  const log = [
    {
      language: 'en-gb',
      user: 'mock user',
      text: 'Hello world',
    },
    {
      language: 'en-gb',
      user: 'mock bot',
      text: 'Hey there',
    }
  ];
  const scrollIntoViewMock = jest.fn();

  beforeEach(() => {
    window.HTMLElement.prototype.scrollIntoView = scrollIntoViewMock;
    render(
      <ChatLog log={log} />
    )
  })

  afterEach(jest.resetAllMocks)

  it("Displays chat log", () => {
    for (const logLine of log) {
      expect(screen.getByText(logLine.text)).toBeInTheDocument()
    }
  })

  it("Scrolls last log line into view", () => {
    expect(scrollIntoViewMock).toHaveBeenCalledTimes(1);
  })
})
