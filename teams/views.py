from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Team, Person
from .serializers import TeamSerializer, PersonSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing commands.

    Includes standard CRUD operations:
    - Create a new team
    - Get a list of teams or detailed information about a single team
    - Update an existing team
    - Delete a team

    Uses TeamSerializer to serialize and deserialize data.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @action(detail=True, methods=['get'])
    def members(self, request, pk=None):
        """
        Gets a list of all members of a specific team.

        This method adds an additional route "/teams/{team_id}/members/", which allows you to
        to get a list of all members of the team specified in the pk parameter.

        Parameters:
        - request: An HttpRequest object representing a request from the user.
        - pk (int, optional): Unique identifier of the team. If specified,
          returns the members of that particular team.

        Returns:
        - Response: A Response object containing a serialized list of team members.
        """
        team = self.get_object()
        members = team.members.all()
        serializer = PersonSerializer(members, many=True)
        return Response(serializer.data)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
