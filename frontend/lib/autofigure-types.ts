// AutoFigure TypeScript Types

export type ContentType = 'paper' | 'survey' | 'blog' | 'textbook'
// Supported LLM providers
export type LLMProvider = 'bianxie' | 'openrouter' | 'gemini' | 'zhipuai' | 'openai' | 'deepseek' | 'siliconflow' | 'custom'
export type EnhancementMode = 'none' | 'code2prompt'
export type SessionStatus = 'idle' | 'generating' | 'waiting_feedback' | 'enhancing' | 'completed' | 'error'

export interface AutoFigureConfig {
    // Content Configuration
    contentType: ContentType
    inputText: string

    // Iteration Parameters
    maxIterations: number
    qualityThreshold: number
    minImprovement: number
    humanInLoop: boolean

    // LLM Configuration (for layout generation)
    llmProvider: LLMProvider
    apiKey: string
    baseUrl?: string
    model: string

    // Output Configuration
    svgWidth: number
    svgHeight: number

    // Methodology Extraction Configuration (for paper content type)
    enableMethodologyExtraction: boolean
    methodologyLlmProvider: LLMProvider
    methodologyLlmApiKey: string
    methodologyLlmBaseUrl?: string
    methodologyLlmModel: string

    // Beautification (shown after layout finalization)
    enhancementMode: EnhancementMode
    artStyle: string
    enhancementCount: number

    // Enhancement LLM Configuration (user-provided, for code2prompt conversion)
    enhancementLlmProvider: LLMProvider
    enhancementLlmApiKey: string
    enhancementLlmBaseUrl?: string
    enhancementLlmModel: string

    // Image Generation API Configuration (user-provided)
    imageGenProvider: LLMProvider
    imageGenApiKey: string
    imageGenBaseUrl?: string
    imageGenModel: string
}

export interface EvaluationScores {
    aesthetic_design: number
    content_fidelity: number
    placeholder_usage: number
}

export interface EvaluationResult {
    scores: EvaluationScores
    overall_quality: number
    critique_summary: string
    specific_issues: string[]
    improvement_suggestions: string[]
}

export interface IterationResult {
    iteration: number
    xml: string
    pngBase64?: string
    evaluation?: EvaluationResult
    humanFeedback?: string
    humanScore?: number
    timestamp: string
}

export interface AutoFigureSession {
    sessionId: string
    status: SessionStatus
    config: AutoFigureConfig
    currentIteration: number
    iterations: IterationResult[]
    finalXml?: string
    finalPngBase64?: string  // PNG preview of user-edited final XML
    enhancedImages?: EnhancedImage[]
    error?: string
}

export interface EnhancedImage {
    variant: number
    pngBase64: string | null
    status: 'pending' | 'processing' | 'completed' | 'failed'
    error?: string
}

export interface StartGenerationResponse {
    sessionId: string
    iteration: number
    xml: string
    pngBase64: string
    status: SessionStatus
}

export interface ContinueIterationRequest {
    currentXml: string
    humanFeedback?: string
    humanScore?: number
}

export interface ContinueIterationResponse {
    iteration: number
    xml: string
    pngBase64: string
    evaluation: EvaluationResult
    status: SessionStatus
}

export interface EnhanceRequest {
    mode: EnhancementMode
    artStyle: string
    variantCount: number
    // User-provided LLM config for code2prompt
    enhancementLlmProvider: LLMProvider
    enhancementLlmApiKey: string
    enhancementLlmBaseUrl?: string
    enhancementLlmModel: string
    // User-provided image generation config
    imageGenProvider: LLMProvider
    imageGenApiKey: string
    imageGenBaseUrl?: string
    imageGenModel: string
}

export interface EnhanceStatusResponse {
    status: 'processing' | 'completed' | 'failed'
    progress: number
    completedVariants: number
    totalVariants: number
    images: EnhancedImage[]
}

// Default configuration values - all API credentials must be provided by user
export const DEFAULT_CONFIG: AutoFigureConfig = {
    contentType: 'paper',
    inputText: '',
    maxIterations: 5,
    qualityThreshold: 9.0,
    minImprovement: 0.2,
    humanInLoop: true,
    llmProvider: 'zhipuai',
    apiKey: '',
    baseUrl: 'https://open.bigmodel.cn/api/paas/v4',
    model: 'glm-4.7-flash',
    svgWidth: 1333,
    svgHeight: 750,
    // Methodology extraction config (for paper content type)
    enableMethodologyExtraction: true,
    methodologyLlmProvider: 'zhipuai',
    methodologyLlmApiKey: '',
    methodologyLlmBaseUrl: 'https://open.bigmodel.cn/api/paas/v4',
    methodologyLlmModel: 'glm-4.7-flash',
    // Beautification config
    enhancementMode: 'code2prompt',
    artStyle: '',  // User must provide their own custom art style description
    enhancementCount: 3,
    // Enhancement LLM config (user must provide)
    enhancementLlmProvider: 'zhipuai',
    enhancementLlmApiKey: '',
    enhancementLlmBaseUrl: 'https://open.bigmodel.cn/api/paas/v4',
    enhancementLlmModel: 'glm-4.7-flash',
    // Image generation config (user must provide)
    imageGenProvider: 'zhipuai',
    imageGenApiKey: '',
    imageGenBaseUrl: 'https://open.bigmodel.cn/api/paas/v4',
    imageGenModel: 'glm-4.7-flash',
}

// LLM Provider configurations
export const LLM_PROVIDERS: Record<LLMProvider, {
    name: string
    defaultBaseUrl: string
    defaultModel: string
    description: string
}> = {
    bianxie: {
        name: 'BianXie',
        defaultBaseUrl: 'https://api.bianxie.ai/v1',
        defaultModel: 'gemini-3.1-pro-preview',
        description: 'BianXie AI API (OpenAI-compatible)',
    },
    openrouter: {
        name: 'OpenRouter',
        defaultBaseUrl: 'https://openrouter.ai/api/v1',
        defaultModel: 'google/gemini-3.1-pro-preview',
        description: 'OpenRouter API - Access multiple AI models',
    },
    gemini: {
        name: 'Google Gemini',
        defaultBaseUrl: 'https://generativelanguage.googleapis.com/v1beta',
        defaultModel: 'gemini-3.1-pro-preview',
        description: 'Google Gemini API - Direct access to Gemini models',
    },
    zhipuai: {
        name: 'ZhipuAI (ZAI)',
        defaultBaseUrl: 'https://open.bigmodel.cn/api/paas/v4',
        defaultModel: 'glm-4.7-flash',
        description: 'ZhipuAI Open Platform - GLM/CogView/CogVideo models',
    },
    openai: {
        name: 'OpenAI',
        defaultBaseUrl: 'https://api.openai.com/v1',
        defaultModel: 'gpt-4o-mini',
        description: 'OpenAI-compatible API (Chat Completions)',
    },
    deepseek: {
        name: 'DeepSeek',
        defaultBaseUrl: 'https://api.deepseek.com/v1',
        defaultModel: 'deepseek-chat',
        description: 'DeepSeek OpenAI-compatible API',
    },
    siliconflow: {
        name: 'SiliconFlow',
        defaultBaseUrl: 'https://api.siliconflow.cn/v1',
        defaultModel: 'Qwen/Qwen2.5-72B-Instruct',
        description: 'SiliconFlow OpenAI-compatible API',
    },
    custom: {
        name: 'Custom',
        defaultBaseUrl: '',
        defaultModel: '',
        description: 'Use any OpenAI-compatible API endpoint',
    },
}
