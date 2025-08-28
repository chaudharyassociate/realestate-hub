# Reconness - Reconnaissance Framework
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Clone Reconness repository
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/reconness/reconness.git .

# Build the application
RUN dotnet restore "src/ReconNess.Web/ReconNess.Web.csproj"
COPY . .
WORKDIR "/src/src/ReconNess.Web"
RUN dotnet build "ReconNess.Web.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "ReconNess.Web.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .

# Copy custom entrypoint
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]